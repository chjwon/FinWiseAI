# FinWiseAI

This project analyzes financial sentiment from news articles, evaluates stock trends, and provides stock recommendations using FinBERT and historical stock data.

## Project Overview

- **Sentiment Analysis**: Uses FinBERT to analyze the sentiment of the latest news related to a specific company.
- **Stock Price Trend Analysis**: Analyzes recent stock price movements to determine the trend.
- **Market Sentiment**: Uses Fear & Greed index data to gauge the overall market sentiment.
- **Stock Recommendation**: Combines news sentiment, stock trends, and market sentiment to make a recommendation: "buy," "sell," or "hold."
- **Custom Modules**:
  - **news.py**: Fetches the latest news articles about the specified company.
  - **stock.py**: Retrieves the recent stock prices for trend analysis.
  - **fear_greed.py**: Obtains the Fear & Greed index to evaluate the overall market sentiment.

## Requirements

```bash
pip install -r requirements.txt
```