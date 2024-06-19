# Stock Sentiment Analysis from News Headlines using ML Algorithms

This project analyzes stock sentiment from news headlines using machine learning algorithms to generate trading signals and evaluate portfolio performance.

## Table of Contents
1. [Introduction](#introduction)
2. [Installation](#installation)
3. [Usage](#usage)
4. [Files Overview](#files-overview)
5. [Results](#results)
6. [Conclusion](#conclusion)

## Introduction
The objective of this project is to predict stock price movements based on sentiment analysis of news headlines. We use Natural Language Processing (NLP) techniques to analyze the sentiment of news articles and generate trading signals based on the sentiment scores.


## Installation
1. Clone the repository:
    ```sh
    git clone https://github.com/Pradipta-Sundar-Sahoo/Stock-Sentiment-Analysis-using-headlines.git
    ```

2. Install the required packages:
    ```sh
    pip install -r requirements.txt
    ```

3. Download NLTK data:
    ```sh
    python -m nltk.downloader vader_lexicon
    ```

## Usage
1. Import the necessary modules:
    ```python
    from data_collection import fetch_news, fetch_stock_data
    from metrics_calc import calculate_max_drawdown, calculate_portfolio_metrics, calculate_sharpe_ratio, plot_signals
    from score_calc import aggregate_sentiment_scores, generate_trading_signals, calculate_sentiment_scores
    from trade_visualise import simulate_trades
    from final import final
    ```

2. Fetch stock data and news headlines:
    ```python
    stock_data = fetch_stock_data("GOOGL")
    news_data = fetch_news("GOOGL")
    ```

3. Calculate sentiment scores and generate trading signals:
    ```python
    news_data_with_scores = calculate_sentiment_scores(news_data)
    sentiment_summary = aggregate_sentiment_scores(news_data_with_scores)
    trading_signals = generate_trading_signals(sentiment_summary)
    ```

4. Simulate trades and visualize results:
    ```python
    portfolio = simulate_trades(stock_data, trading_signals, initial_capital=10000)
    plot_signals(stock_data, portfolio, "GOOGL")
    ```

5. Run the final script:
    ```python
    final("GOOGL", risk_free_rate=0.01, initial=10000, df=news_data)
    ```

## Files Overview
- **b_data_collection.py**: Fetches stock prices and news headlines.
- **a_metrics_calc.py**: Calculates performance metrics like total trades, win percentage, total profit, Sharpe ratio, and maximum drawdown.
- **c_score_calc.py**: Performs sentiment analysis on news headlines and generates trading signals.
- **d_trade_visualise.py**: Simulates trades based on trading signals and visualizes the results.
- **e_final.py**: Integrates all components to fetch data, calculate sentiment, generate signals, simulate trades, and calculate metrics.

## Results
The project outputs include the following:
- Total number of trades
- Win percentage
- Total profit
- Sharpe ratio
- Maximum drawdown
- Visualizations of buy/sell signals on stock price charts

![GOOGL](https://github.com/Pradipta-Sundar-Sahoo/Stock-Sentiment-Analysis-using-headlines/assets/157369477/8a6a19d5-a5e0-4ec2-8a8a-df00a70b5456)

![image](https://github.com/Pradipta-Sundar-Sahoo/Stock-Sentiment-Analysis-using-headlines/assets/157369477/bc041559-4e7e-4baf-913c-11dd55fdda0a)

## Conclusion
This project demonstrates how sentiment analysis of news headlines can be used to predict stock price movements and make informed trading decisions. The trading strategy's performance is evaluated using various financial metrics, providing insights into its effectiveness.

For more details open 22118054_FC24OPS3.pdf.

