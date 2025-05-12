def fib_confluence_strategy(df):
    df['Retrace'] = (df['close'] - df['low'].rolling(20).min()) / (df['high'].rolling(20).max() - df['low'].rolling(20).min())
    df['Signal'] = df['Retrace'].between(0.5, 0.618)
    return df[df['Signal']]