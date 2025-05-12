def momentum_strategy(df, debug=False):
    import ta
    df = df.copy()
    macd_diff = ta.trend.MACD(df['close']).macd_diff()
    df['macd_diff'] = macd_diff.squeeze()
    df.dropna(subset=['macd_diff'], inplace=True)
    df['Signal'] = df['macd_diff'] > 0
    if debug:
        print(f"[Momentum] {df['Signal'].sum()} signals found")
    return df[df['Signal']]