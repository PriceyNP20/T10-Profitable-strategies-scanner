import yfinance as yf

def get_data(symbol, period="3mo", interval="1d"):
    df = yf.download(tickers=symbol, period=period, interval=interval)
    df.reset_index(inplace=True)
    df.columns = [col.lower() for col in df.columns]
    return df