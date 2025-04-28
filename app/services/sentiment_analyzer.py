# Этот файл отвечает за работу с моделью анализа тональности текста на русском языке.

from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch

# Загружаю токенизатор и модель с Hugging Face
tokenizer = AutoTokenizer.from_pretrained("blanchefort/rubert-base-cased-sentiment")
model = AutoModelForSequenceClassification.from_pretrained("blanchefort/rubert-base-cased-sentiment")

# Словарь для преобразования индекса в понятный текст
id2label = {0: "negative", 1: "neutral", 2: "positive"}

# Функция для анализа текста
def analyze_sentiment(text: str) -> str:
    """
    Принимаю на вход текст, токенизирую его, пропускаю через модель,
    и возвращаю метку: 'positive', 'neutral', 'negative'.
    """
    inputs = tokenizer(text, return_tensors="pt", truncation=True, max_length=512)
    with torch.no_grad():
        outputs = model(**inputs)
    logits = outputs.logits
    prediction = torch.argmax(logits, dim=-1)
    sentiment = id2label[prediction.item()]
    return sentiment
