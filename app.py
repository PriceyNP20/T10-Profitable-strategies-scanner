import streamlit as st
from src.utils.fetch_data import get_data
from src.strategies.trend_following import trend_following_strategy

st.title("Top 10 Profitable Trading Strategies")

symbol = st.text_input("Symbol (e.g., BTC-USD)", "BTC-USD")
df = get_data(symbol)

st.subheader("Trend Following Signal")
signals = trend_following_strategy(df)
st.dataframe(signals.tail())