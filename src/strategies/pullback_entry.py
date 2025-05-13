def pullback_entry_strategy(df):
    df = df.copy()
    df['MA50'] = df['close'].rolling(50).mean()
    df['Signal'] = (df['close'] > df['MA50']) & (df['close'].shift(1) < df['MA50'])
    return df[df['Signal']]
pullback_entry_strategy = pullback_entry_strategy
