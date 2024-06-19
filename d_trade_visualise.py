import pandas as pd
from b_fetch_data import fetch_news, fetch_stock_data
def simulate_trades(stock_data, trading_signals,capital):
    portfolio = []
    position = 0
    buy_price = 0
    quantity =0
    for date, price in (stock_data['Close'].items()):
        if date in trading_signals.index:
            signal = trading_signals.loc[date]
            if signal == 1 and position == 0:  # Buy signal
                position = 1
                buy_price = price
                quantity = capital/price
                capital = capital%price
                portfolio.append({"date": date, "type": "buy", "price": buy_price, "capital":capital})
            elif signal == -1 and position == 1 and (price>buy_price) :  # Sell signal
                position = 0
                sell_price = price
                profit = (sell_price - buy_price)*quantity
                capital = capital+ quantity*sell_price
                portfolio.append({"date": date, "type": "sell", "price": sell_price,"capital":capital, "profit": profit})

    return pd.DataFrame(portfolio)
