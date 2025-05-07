from paddleocr import PaddleOCR
from PIL import Image
import numpy as np
import gradio as gr
import ollama
import io
import re

#Local imports
from examples import examples as examples_raw
from theme.factify_theme import custom_theme


# Initialize PaddleOCR (CPU version)
ocr_engine = PaddleOCR(use_angle_cls=True, lang='en', use_gpu=False)

def build_prompt(headline, article):
    return f"""
You are a fact-checking assistant.

Please analyze the following news article and determine whether it is REAL or FAKE based on your general knowledge. Also provide a confidence score (0–1) and a short explanation.

News Headline:
{headline}

News Content:
{article}

Return your response in this format:
Here's my full analysis: 

Label: REAL or FAKE
Confidence: [1% to 100%]
Reason: [short explanation]
"""

def extract_text_from_image(img):
    try:
        img_pil = Image.fromarray(img).convert("RGB")
        img_np = np.array(img_pil)
        result = ocr_engine.ocr(img_np, cls=True)
        extracted_lines = [line[1][0] for line in result[0]]
        if len(extracted_lines) < 2:
            return None, None
        headline = extracted_lines[0]
        article = ' '.join(extracted_lines[1:])
        return headline, article
    except Exception as e:
        return None, None

def classify_input(image, headline, article):
    if image is not None and isinstance(image, np.ndarray):
        headline, article_text = extract_text_from_image(image)
        if not headline or not article_text:
            return "Could not extract enough text from image."
    else:
        if not headline or not article:
            return "Please provide either an image or both text fields."
        article_text = article

    prompt = build_prompt(headline, article_text)

    try:
        response = ollama.chat(
            model='llama3',
            messages=[{"role": "user", "content": prompt}]
        )
        content = response['message']['content']
        label, confidence, explanation = extract_facts(content)
        return label, confidence, explanation
    except Exception as e:
        return "ERROR", "N/A", f"Error: {e}"

def extract_facts(llm_response):
    label = "UNKNOWN"
    confidence = "N/A"
    explanation = llm_response.strip()

    # Extract label
    label_match = re.search(r"Label:\s*(REAL|FAKE)", llm_response, re.IGNORECASE)
    if label_match:
        label = label_match.group(1).upper()

    # Extract confidence
    conf_match = re.search(r"Confidence:\s*(\d+%?)", llm_response)
    if conf_match:
        confidence = conf_match.group(1)

    # Extract reason (optional improvement)
    reason_match = re.search(r"Reason:\s*(.+)", llm_response, re.DOTALL)
    if reason_match:
        explanation = reason_match.group(1).strip()

    return label, confidence, explanation

# For display purposes only
examples_for_display = [
    [
        img,
        headline if headline else "N/A",
        article if article else "N/A"
    ]
    for img, headline, article in examples_raw
]

# Gradio UI layout
with gr.Blocks(theme=custom_theme, fill_height=True) as demo:
    # Orange Header
    gr.Markdown(
        "<h1 style='text-align:center; color:#ea580c;'>Factify: Fake News Classifier</h1>"
    )
    
    # Orange Subheader
    gr.Markdown(
        "<h3 style='text-align:center; color:#ea580c;'>Upload a news screenshot or paste the headline + article below</h3>"
    )

    with gr.Row():
        with gr.Column():
            image_input = gr.Image(label="Upload News Image (Optional)", type="numpy")
            headline_input = gr.Textbox(label="Headline", placeholder="Enter the news headline or N/A")
            article_input = gr.Textbox(label="Full Article", lines=10, placeholder="Paste the article text or N/A")
            submit_btn = gr.Button("🔍 Analyze", elem_id="analyze-btn")

        with gr.Column():
            output_label = gr.Textbox(label="Prediction (Real or Fake)")
            confidence_score = gr.Textbox(label="Confidence Score")
            llm_explanation = gr.Textbox(label="LLM Explanation", lines=6)

    submit_btn.click(
        fn=classify_input,
        inputs=[image_input, headline_input, article_input],
        outputs=[output_label, confidence_score, llm_explanation]
    )

    with gr.Accordion("Try Examples", open=False):
        try:
            from examples import examples
            gr.Examples(
                examples=examples_for_display,
                inputs=[image_input, headline_input, article_input],
                label="Try these examples"
            )
        except Exception:
            gr.Markdown("No examples loaded.")

if __name__ == "__main__":
    demo.launch()
