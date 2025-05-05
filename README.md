# Factify — Fake News Classifier

Factify is a lightweight AI-powered application that classifies news articles as **REAL** or **FAKE** using both **text input** and **image-based content**.

It combines:
- `PaddleOCR` for extracting text from images
- `Ollama` for running local LLMs like TinyLLaMA or larger models like Llama3
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

> Works on **Windows** and **macOS**
> Tested with **Python 3.10** (not compatible with Python 3.12+)
> **Python 3.10** used to run PaddleOCR smoothly.

---

### Step 1: Install Python 3.10

Factify requires Python 3.10 for compatibility with PaddleOCR and other tools. Follow these steps to install and use it.

#### Download and Install Python 3.10

Download it here:  
https://www.python.org/downloads/release/python-3100/

#####  Windows

1. Download Windows Installer (64-bit).
2. Check "Add Python 3.10 to PATH" during installation.
3. Enable pip and environment variables.
4. Complete the install.

Verify:

```bash
python --version
# Should output: Python 3.10.x
```
##### MacOS

brew install python@3.10
echo 'alias python="python3.10"' >> ~/.zshrc
source ~/.zshrc

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
