def momentum_strategy(df):
    import ta
    df = df.copy()
    df['macd'] = ta.trend.MACD(df['close'].squeeze()).macd_diff()
    df['Signal'] = df['macd'] > 0
    return df[df['Signal']]
momentum_strategy = momentum_strategy
