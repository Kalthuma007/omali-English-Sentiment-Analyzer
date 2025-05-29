import warnings
from urllib3.exceptions import NotOpenSSLWarning

warnings.filterwarnings("ignore", category=NotOpenSSLWarning)
from textblob import TextBlob
from langdetect import detect
from transformers import pipeline
import re

# Specify the model explicitly to avoid the HF warning
hf_sentiment = pipeline(
    "sentiment-analysis",
    model="distilbert-base-uncased-finetuned-sst-2-english"
)

def somali_sentiment(text):
    positive_words = [
        "wanaagsan", "fiican", "farxad", "mahadsanid",
        "guul", "guulaystay", "guuleystay", "guulaysatay", "ku guulaystay",
        "horumar", "farxad leh", "guulaysaty", "qurx","quruxsan", "nabad", "nabadgelyo",
        "nabadgelyo leh", "nabadgelyada", "nabadgelyada leh", "nabadgelyo wanaagsan",
        "nabadgelyo wanaagsan", "nabadgelyo fiican", "nabadgelyo wanaagsan", "nabadgelyo fiican",'quruxbadan'
    ]
    negative_words = [
    "xun", "nacayb", "murugo", "cadho",
    "doqon", "foolxun", "fulayad", "dhacday", "guuldaraysatay","doqon","doqoniimo",
]


    text_lower = text.lower()
    pos_count = sum(word in text_lower for word in positive_words)
    neg_count = sum(word in text_lower for word in negative_words)

    # Check for reward pattern like "$200" or "200$" or the word "guul" (win)
    reward_pattern = re.compile(r"\$\d+|\d+\$|\bguul\b")
    if reward_pattern.search(text_lower):
        pos_count += 1

    if pos_count > neg_count:
        return "Positive"
    elif neg_count > pos_count:
        return "Negative"
    else:
        return "Neutral"

def analyze_sentiment(text):
    try:
        lang = detect(text)
    except:
        lang = "unknown"

    if lang == "en":
        result = hf_sentiment(text)[0]
        return result["label"]
    elif lang == "so":
        return somali_sentiment(text)
    else:
        blob = TextBlob(text)
        polarity = blob.sentiment.polarity
        if polarity > 0:
            return "Positive"
        elif polarity < 0:
            return "Negative"
        else:
            return "Neutral"
