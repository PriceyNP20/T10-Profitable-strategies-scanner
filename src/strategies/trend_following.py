def trend_following_strategy(df, fast=50, slow=200):
    df['MA_Fast'] = df['close'].rolling(fast).mean()
    df['MA_Slow'] = df['close'].rolling(slow).mean()
    df['Signal'] = (df['MA_Fast'] > df['MA_Slow']) & (df['MA_Fast'].shift(1) <= df['MA_Slow'].shift(1))
    return df[df['Signal']]