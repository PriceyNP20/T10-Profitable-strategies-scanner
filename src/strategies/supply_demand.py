def supply_demand_strategy(df, debug=False):
    df = df.copy()
    df['Demand_Zone'] = df['low'].rolling(5).min()
    df.dropna(subset=['Demand_Zone', 'close'], inplace=True)
    df['Signal'] = df['close'] <= df['Demand_Zone']
    if debug:
        print(f"[Supply & Demand] {df['Signal'].sum()} signals found")
    return df[df['Signal']]