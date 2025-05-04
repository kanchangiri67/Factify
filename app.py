from paddleocr import PaddleOCR
from PIL import Image
import numpy as np
import gradio as gr
import ollama
import io
from examples import examples

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
Label: REAL or FAKE
Confidence: [0.0 to 1.0]
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
    if image is not None:
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
        return response['message']['content']
    except Exception as e:
        return f"Error: {e}"

iface = gr.Interface(
    fn=classify_input,
    inputs=[
        gr.Image(label="🖼️ Upload News Image (Optional)", type="numpy"),
        gr.Textbox(label="📰 Headline", lines=1, placeholder="Enter headline if not using image"),
        gr.Textbox(label="🧾 Article Content", lines=6, placeholder="Enter article content if not using image")
    ],
    outputs=gr.Textbox(label="📣 Factify's Verdict"),
    title="Factify — Fake News Classifier",
    description=(
        "**Factify** uses PaddleOCR to read image-based news and LLaMA 3 (via Ollama) to evaluate whether it is **REAL or FAKE**, with a confidence score and explanation.\n\n"
        "💡 Upload an image or enter text manually. Powered by local AI models."
    ),
    examples=examples,  # using the imported variable
    allow_flagging="never",
    theme="default"
)

if __name__ == "__main__":
    iface.launch()
