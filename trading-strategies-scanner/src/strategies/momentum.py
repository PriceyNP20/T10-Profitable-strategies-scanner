def momentum_strategy(df):
    import ta
    df['macd'] = ta.trend.MACD(df['close']).macd_diff()
    df['Signal'] = df['macd'] > 0
    return df[df['Signal']]