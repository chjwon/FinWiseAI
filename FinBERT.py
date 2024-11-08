from fear_greed import get_fear_greed
from news import get_3_news
from stock import get_7_stockprice



from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch
import numpy as np


model_name = "ProsusAI/finbert"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSequenceClassification.from_pretrained(model_name)

def analyze_sentiment(news_list):
    inputs = tokenizer(news_list, padding=True, truncation=True, return_tensors='pt')
    outputs = model(**inputs)
    predictions = torch.nn.functional.softmax(outputs.logits, dim=-1)
    sentiment_scores = predictions.detach().numpy()
    return sentiment_scores

def aggregate_sentiment(sentiment_scores):
    average_scores = np.mean(sentiment_scores, axis=0)
    sentiment = {
        'positive': average_scores[0],
        'negative': average_scores[1],
        'neutral': average_scores[2]
    }
    return sentiment

def analyze_stock_trend(stock_prices):
    if len(stock_prices) < 2:
        return 'neutral'
    trend = np.polyfit(range(len(stock_prices)), stock_prices, 1)[0]
    if trend > 0:
        return 'upward'
    elif trend < 0:
        return 'downward'
    else:
        return 'neutral'

def get_recommendation(company_ticker):
    market_sentiment = get_fear_greed()

    news_list = get_3_news(company_ticker)

    sentiment_scores = analyze_sentiment(news_list)
    news_sentiment = aggregate_sentiment(sentiment_scores)

    stock_prices = get_7_stockprice(company_ticker)

    stock_trend = analyze_stock_trend(stock_prices)

    # Decision logic # need ref and change it
    if news_sentiment['positive'] > news_sentiment['negative'] and stock_trend == 'upward' and market_sentiment > 50:
        return 'buy'
    elif news_sentiment['negative'] > news_sentiment['positive'] and stock_trend == 'downward' and market_sentiment < 50:
        return 'sell'
    else:
        return 'hold'

company_ticker = "AAPL"
recommendation = get_recommendation(company_ticker)
print(f"The recommendation for {company_ticker} is to: {recommendation}")
