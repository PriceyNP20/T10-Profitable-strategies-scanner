import yfinance as yf
import pandas as pd

def get_data(symbol, period="3mo", interval="1d"):
    df = yf.download(tickers=symbol, period=period, interval=interval)

    # Ensure standard column names regardless of how yfinance structures them
    df = df.rename(columns={
        'Open': 'open',
        'High': 'high',
        'Low': 'low',
        'Close': 'close',
        'Adj Close': 'adj_close',
        'Volume': 'volume'
    })

    df.reset_index(inplace=True)
    return df
