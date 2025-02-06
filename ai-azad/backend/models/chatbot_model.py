# backend/models/chatbot_model.py

from transformers import pipeline

def generate_response(question):
    chatbot = pipeline("conversational", model="microsoft/DialoGPT-medium")
    response = chatbot(question)
    return response['generated_text']