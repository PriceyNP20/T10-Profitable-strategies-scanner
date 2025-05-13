def supply_demand_strategy(df):
    df = df.copy()
    df['Demand_Zone'] = df['low'].rolling(5).min()
    df['Signal'] = df['close'] <= df['Demand_Zone']
    return df[df['Signal']]
supply_demand_strategy = supply_demand_strategy
