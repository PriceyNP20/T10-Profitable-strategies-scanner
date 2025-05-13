import streamlit as st
import pandas as pd
from src.utils.fetch_data import get_data
from src.strategies.plot_signal_chart import plot_signal_chart

# === Your strategy imports go here ===
# from src.strategies.trend_following import trend_following_strategy
# from src.strategies.breakout import breakout_strategy
# etc...

st.title("Top 10 Profitable Trading Strategies")
symbols = ["BTC-USD", "ETH-USD", "BNB-USD", "XRP-USD", "SOL-USD"]

# Replace with your strategy mapping
def dummy_strategy(df):
    df = df.copy()
    df["Signal"] = df["close"] > df["close"].shift(1)
    matches = df[df["Signal"]]
    matches["Timestamp"] = matches.index
    matches["Entry"] = matches["close"]
    matches["StopLoss"] = matches["close"] * 0.98
    matches["TakeProfit"] = matches["close"] * 1.05
    matches["SignalType"] = "Long"
    return matches[["Timestamp", "Entry", "StopLoss", "TakeProfit", "SignalType"]]

selected_strategy = dummy_strategy

results = []
for symbol in symbols:
    try:
        df = get_data(symbol)
        signals_df = selected_strategy(df)
        results.append({"symbol": symbol, "matches": len(signals_df), "details": signals_df.to_dict(orient="records")})
    except Exception as e:
        results.append({"symbol": symbol, "error": str(e)})

# === Display Results ===
for res in results:
    if "error" in res:
        st.error(f"{res['symbol']}: {res['error']}")
    else:
        st.markdown(f"### {res['symbol']} — Matches: {res.get('matches', 0)}")
        if res.get("details"):
            df = pd.DataFrame(res["details"])
            st.dataframe(df)
            with st.expander("📈 View Chart"):
                fig = plot_signal_chart(df)
                st.plotly_chart(fig, use_container_width=True)
