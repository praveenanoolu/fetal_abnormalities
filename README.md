# Fetal Abnormalities Detection Web App

This Streamlit-based web app allows users to upload fetal ultrasound images and receive real-time AI analysis for potential abnormalities. It integrates both a vision model and an LLM to offer expert-like medical interpretation.

## Features
- Upload ultrasound images in JPG/PNG format
- Deep learning model (EfficientNet) for anomaly detection
- Medical-grade explanation via LLM (Groq API)

## Setup Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/your-repo/fetal_abnormalities.git
cd fetal_abnormalities/python-prototype
```

### 2. Create Virtual Environment
```bash
python -m venv .venv
source .venv/bin/activate  # or .venv\Scripts\activate on Windows
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Set Groq API Key
Create an `.env` file or export manually:
```bash
export GROQ_API_KEY="your-groq-key-here"
```

### 5. Run the Web App
```bash
streamlit run src/main.py
```

## Project Structure
```
python-prototype/
├── src/
│   ├── main.py           # Streamlit interface
│   ├── model/
│   │   ├── model.py      # ML model logic
│   │   └── utils.py      # (Reserved for helper functions)
│   └── llm/
│       └── expert.py     # Groq LLM integration
```

## Notes
- Replace mock model logic with fine-tuned classifier for real deployment.
- Ensure GROQ_API_KEY is valid to get LLM responses.