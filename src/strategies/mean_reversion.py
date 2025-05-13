def mean_reversion_strategy(df, rsi_period=14):
    import ta
    df = df.copy()
    df['rsi'] = ta.momentum.RSIIndicator(df['close'].squeeze(), window=rsi_period).rsi()
    df['Signal'] = df['rsi'] < 30
    return df[df['Signal']]