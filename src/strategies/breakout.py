    df = df.copy()
    df['High_Max'] = df['high'].rolling(length).max()
    df['High_Max_shifted'] = df['High_Max'].shift(1)
    df['Breakout'] = df['close'] > df['High_Max_shifted']
    return df[df['Breakout']]
breakout_strategy = breakout_strategy
