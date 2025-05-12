def liquidity_sweep_strategy(df):
    df['Sweep'] = (df['low'] < df['low'].shift(1)) & (df['close'] > df['open'])
    return df[df['Sweep']]