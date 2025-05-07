# Factify — Fake News Classifier

Factify is a lightweight AI-powered application that classifies news articles as **REAL** or **FAKE** using both **text input** and **image-based content**.

It combines:
- `PaddleOCR` for extracting text from images
- `Ollama` for running local LLMs like TinyLLaMA or larger models like Llama3
- `Gradio` to provide a sleek and interactive web UI

How it Works:

- Upload a news screenshot or type in a headline + article
- PaddleOCR reads the text (if image is uploaded)
- If text input is submitted, the model directly uses llama3 as image-to-text generation is not needed.
- Ollama uses large language model LLM, llama3, to analyze the content. The llama3 model is given a custom prompt to act like a fact-checking assistant each time the user provides input.

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

##### MacOS command for installation of Python version 3.10

``` bash
brew install python@3.10 # if using brew for installation
echo 'alias python="python3.10"' >> ~/.zshrc
source ~/.zshrc
```

### Step 2: Install Ollama

- Visit: https://ollama.com/download
- Download and install Ollama for your OS
- Start Ollama in the background 

``` bash
ollama run llama3 # How to run llama3 using ollama
```

---

### Step 3: Clone the project and Navigate to it

```bash
git clone https://github.com/yourusername/factify.git
cd FACTIFY
```
---

### Step 4: Create and Activate a Virtual Environment

#### Create virtual environment with Python 3.10

``` bash
python -3.10 -m venv venv
```

#### Activate it
```bash
venv\Scripts\activate         # On Windows
```
#### OR
```bash
source venv/bin/activate      # On Mac/Linux
```

It is better to have a conda environment set up to use the PaddleOCR for text-to-image generation. Conda environment allows better threading via PaddlePaddle and can automatically use multiple CPU cores if available in the local machine. Below are the instructions for activating conda environment with Python 3.10. 

```bash
conda create -n paddle_env python=3.10 # Potentially need to install conda and if the application is not already installed
conda activate paddle_env
```

---

### Step 5: Install Requirements

```bash
pip install --upgrade pip
pip install -r requirements.txt
```
---

### Step 6: Run the App
```bash
python app.py
```
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
