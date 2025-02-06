# backend/models/roberta_model.py

from transformers import pipeline

def classify_text(text):
    sentiment_pipeline = pipeline("sentiment-analysis", model="nlptown/bert-base-multilingual-uncased-sentiment")
    result = sentiment_pipeline(text)[0]
    return result['label']