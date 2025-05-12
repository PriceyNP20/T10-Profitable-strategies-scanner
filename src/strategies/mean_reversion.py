def mean_reversion_strategy(df, rsi_period=14, debug=False):
    import ta
    df = df.copy()
    rsi = ta.momentum.RSIIndicator(df['close'], window=rsi_period).rsi()
    df['rsi'] = rsi if rsi.ndim == 1 else rsi.squeeze()
    df.dropna(subset=['rsi'], inplace=True)
    df['Signal'] = df['rsi'] < 30
    if debug:
        print(f"[Mean Reversion] {df['Signal'].sum()} signals found")
    return df[df['Signal']]