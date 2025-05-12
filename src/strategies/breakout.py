def breakout_strategy(df, length=20, debug=False):
    df = df.copy()
    df['High_Max'] = df['high'].rolling(length).max()
    df['High_Max_shifted'] = df['High_Max'].shift(1)
    df.dropna(subset=['close', 'High_Max_shifted'], inplace=True)
    df['Signal'] = df['close'] > df['High_Max_shifted']
    if debug:
        print(f"[Breakout] {df['Signal'].sum()} signals found")
    return df[df['Signal']]