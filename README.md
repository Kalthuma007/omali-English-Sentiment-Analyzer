
# Somali-English Sentiment Analyzer

A web app that performs sentiment analysis on Somali and English text.  
Built using Flask, Hugging Face transformers, TextBlob, and a simple Somali rule-based sentiment logic.

---

## Features

- Detects the language of the input text (Somali or English).
- Uses a pre-trained Hugging Face sentiment model for English text.
- Applies a rule-based approach to analyze Somali sentiment.
- Falls back to TextBlob for other languages.
- Simple and lightweight Flask web interface.

---

## File Structure

```
somali_english_sentiment/
│
├── app.py                  # Flask web app
├── sentiment_analyzer.py  # Sentiment analysis logic
├── templates/
│   └── index.html         # HTML interface
├── static/
│   └── style.css          # Optional CSS styles
├── requirements.txt       # Python dependencies
└── README.md              # Project documentation
```

---

## Installation

1. Clone the repository:

```bash
git clone https://github.com/Kalthuma007/omali-English-Sentiment-Analyzer/tree/main
2. Create and activate a virtual environment:

```bash
python3 -m venv venv
source venv/bin/activate   # For Mac/Linux
# For Windows: venv\Scripts\activate
```

3. Install required packages:

```bash
pip install -r requirements.txt
```

---

## Usage

Run the Flask app:

```bash
python app.py
```

Open your browser and go to:  
http://127.0.0.1:5000/

Enter Somali or English text, then click **Analyze Sentiment** to see the result.

---

## Somali Sentiment Logic

The Somali sentiment analyzer uses a list of positive and negative keywords:

- **Positive**: wanaagsan, fiican, farxad, mahadsanid, ku guulaysaty  
- **Negative**: xun, nacayb, murugo, cadho, doqon, foolxun, fulayad, dhacday, guuldaraysatay

---

## Notes

- The English sentiment analysis uses Hugging Face’s `distilbert-base-uncased-finetuned-sst-2-english` model.
- The app falls back to TextBlob sentiment if the language is not Somali or English.
- For production deployment, consider setting up a production-ready server instead of Flask’s built-in server.

---

## License

This project is open source and available under the MIT License.

Made by **Kaltun Mustafe Mohamed**  

