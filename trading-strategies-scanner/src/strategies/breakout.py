def breakout_strategy(df, length=20):
    df['High_Max'] = df['high'].rolling(length).max()
    df['Breakout'] = df['close'] > df['High_Max'].shift(1)
    return df[df['Breakout']]