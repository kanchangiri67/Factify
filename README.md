# Factify — Fake News Classifier

Factify is a lightweight AI-powered application that classifies news articles as **REAL** or **FAKE** using both **text input** and **image-based content**.

It combines:
- `PaddleOCR` for extracting text from images
- `Ollama` for running local LLMs like TinyLLaMA
- `Gradio` to provide a sleek and interactive web UI

How it Works:

- Upload a news screenshot or type in a headline + article
- PaddleOCR reads the text (if image is uploaded)
- Ollama uses an LLM (like TinyLLaMA) to analyze the content

You get:

- A prediction (REAL or FAKE)
- Confidence score
- Reasoning

---

## Step-by-Step Setup Guide

> Works on **Windows**, **macOS**, and **Linux**  
> Tested with **Python 3.10** (not compatible with Python 3.12+)

---

### Step 1: Install Python 3.10

- Download from: https://www.python.org/downloads/release/python-3100/ for your OS

---

### Step 2: Install Ollama

- Visit: https://ollama.com/download
- Download and install Ollama for your OS
- Start Ollama in the background (ollama run llama3)

---

### Step 3: Clone the project and Navigate to it
git clone https://github.com/yourusername/factify.git
cd factify

---

### Step 4: Create and Activate a Virtual Environment

#### Create virtual environment
python -m venv venv

#### Activate it
venv\Scripts\activate         # On Windows
#### OR
source venv/bin/activate      # On Mac/Linux

---

### Step 5: Install Requirements
pip install --upgrade pip
pip install -r requirements.txt

---

### Step 6: Run the App
python app.py

---

## Project Structure
```
FACTIFY/
└── root/
├── pycache/ # Compiled Python cache
├── flagged/ # Gradio logs or flagged outputs
├── images/ # Sample news screenshots
│ ├── article1.jpeg
│ ├── article2.png
│ └── article4.jpg
├── venv/ # Python virtual environment (not pushed to Git)
├── app.py # Main application
├── examples.py # Gradio preloaded examples
├── README.md # Project documentation
└── requirements.txt # Python dependencies
```
