import yfinance as yf
import pandas as pd

def get_data(symbol, period="3mo", interval="1d"):
    df = yf.download(tickers=symbol, period=period, interval=interval)

    # Handle multi-index columns and extract only the value part (like 'Close', 'Open')
    if isinstance(df.columns, pd.MultiIndex):
        df.columns = [col[1].lower() if col[1] else col[0].lower() for col in df.columns.values]
    else:
        df.columns = [col.lower() for col in df.columns]

    df.reset_index(inplace=True)
    return df

