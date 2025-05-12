import yfinance as yf
import pandas as pd

def get_data(symbol, period="3mo", interval="1d"):
    df = yf.download(tickers=symbol, period=period, interval=interval)

    # Flatten multi-index columns if needed
    if isinstance(df.columns, pd.MultiIndex):
        df.columns = ['_'.join(col).lower() for col in df.columns.values]
    else:
        df.columns = [col.lower() for col in df.columns]

    df.reset_index(inplace=True)
    return df
