def pullback_entry_strategy(df, debug=False):
    df = df.copy()
    df['MA50'] = df['close'].rolling(50).mean()
    df.dropna(subset=['MA50', 'close'], inplace=True)
    df['Signal'] = (df['close'] > df['MA50']) & (df['close'].shift(1) < df['MA50'])
    if debug:
        print(f"[Pullback Entry] {df['Signal'].sum()} signals found")
    return df[df['Signal']]