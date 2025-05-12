def momentum_strategy(df):
    import ta
    macd = ta.trend.MACD(df['close'])
    df['macd_diff'] = macd.macd_diff()
    df['Signal'] = df['macd_diff'] > 0
    return df[df['Signal']]
