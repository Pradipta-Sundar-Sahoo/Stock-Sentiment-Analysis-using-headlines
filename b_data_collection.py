from bs4 import BeautifulSoup
import requests
import pandas as pd
import yfinance as yf
from tqdm.notebook import tqdm
import numpy as np
import matplotlib.pyplot as plt
def fetch_stock_data(ticker):
    print(f'Fetching stock prices for {ticker} ...')
    stock_data = yf.download(ticker, period = "max")
    stock_data = stock_data[['Close']]
    return stock_data

def fetch_news(ticker):
    print(f'Fetching news for {ticker}...')
    columns = ['datetime','ticker','source', 'headline' ]
    df = pd.DataFrame(columns=columns)
    counter = 0
    ticker = str(ticker).lower()
    print("Fetching news headlines...")
    for page in tqdm(range(1,10)):
        url = f'https://markets.businessinsider.com/news/{ticker}-stock?p={page}'
        response = requests.get(url)
        html = response.text
        soup = BeautifulSoup (html, 'lxml')
        articles = soup.find_all('div', class_ = 'latest-news__story')
        for article in articles:
            datetime = article.find('time', class_ = 'latest-news__date').get('datetime')
            title = article.find('a', class_ = 'news-link').text
            source = article.find('span', class_ = 'latest-news__source').text
            ticker=ticker
            df = pd.concat([pd.DataFrame([[datetime,ticker, source,title]], columns=df.columns), df], ignore_index=True)
            counter += 1
               
    df['datetime'] = pd.to_datetime(df['datetime'])
    df['date'] = df['datetime'].dt.date
    df['time'] = df['datetime'].dt.time
    df.drop(columns=['datetime'], inplace=True)
    print (f'{counter} headlines scraped from {page+1} pages')
    return df
