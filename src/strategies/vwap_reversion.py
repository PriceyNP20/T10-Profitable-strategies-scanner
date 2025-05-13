def vwap_reversion_strategy(df):
    df = df.copy()
    df['cum_vol'] = df['volume'].cumsum()
    df['cum_price_vol'] = (df['close'] * df['volume']).cumsum()
    df['vwap'] = df['cum_price_vol'] / df['cum_vol']
    df['Signal'] = df['close'] < df['vwap'] * 0.98
    return df[df['Signal']]
vwap_reversion_strategy = vwap_reversion_strategy
