def vwap_reversion_strategy(df, debug=False):
    df = df.copy()
    df['cum_vol'] = df['volume'].cumsum()
    df['cum_price_vol'] = (df['close'] * df['volume']).cumsum()
    df['vwap'] = df['cum_price_vol'] / df['cum_vol']
    df.dropna(subset=['vwap'], inplace=True)
    df['Signal'] = df['close'] < df['vwap'] * 0.98
    if debug:
        print(f"[VWAP Reversion] {df['Signal'].sum()} signals found")
    return df[df['Signal']]