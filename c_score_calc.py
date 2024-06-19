from bs4 import BeautifulSoup
import requests
import pandas as pd
import yfinance as yf
from tqdm.notebook import tqdm
import numpy as np
import matplotlib.pyplot as plt
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer
nltk.download('vader_lexicon')
# Initialize sentiment analyzer
analyzer = SentimentIntensityAnalyzer()

def calculate_sentiment_scores(headlines_df):
    headlines_df['sentiment'] = headlines_df['headline'].apply(lambda x: analyzer.polarity_scores(x)['compound'])
    headlines_df['date'] = pd.to_datetime(headlines_df['date'])
    
    return headlines_df

def aggregate_sentiment_scores(headlines_df):
    sentiment_summary = headlines_df.groupby('date')['sentiment'].mean()
    return sentiment_summary

def generate_trading_signals(sentiment_summary):
    signals = sentiment_summary.apply(lambda x: 1 if x > 0.15 else (-1 if x < -0.15 else 0))
    return signals