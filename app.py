from src.strategies.plot_signal_chart import plot_signal_chart
from src.strategies.plot_signal_chart import plot_signal_chart

import streamlit as st
import pandas as pd
from src.utils.fetch_data import get_data

# Import all strategies
from src.strategies.trend_following import trend_following_strategy
from src.strategies.breakout import breakout_strategy
from src.strategies.mean_reversion import mean_reversion_strategy
from src.strategies.supply_demand import supply_demand_strategy
from src.strategies.momentum import momentum_strategy
from src.strategies.fib_confluence import fib_confluence_strategy
from src.strategies.vwap_reversion import vwap_reversion_strategy
from src.strategies.options_selling import options_selling_stub
from src.strategies.pullback_entry import pullback_entry_strategy
from src.strategies.liquidity_sweep import liquidity_sweep_strategy

st.title("Multi-Symbol Strategy Scanner")

# Strategy dropdown
strategy_name = st.selectbox("Select Strategy", list(['Trend Following', 'Breakout', 'Mean Reversion', 'Supply & Demand', 'Momentum', 'Fibonacci Confluence', 'VWAP Reversion', 'Options Selling (Stub)', 'Pullback Entry', 'Liquidity Sweep']))
strategy_func = eval({'Trend Following': 'trend_following_strategy', 'Breakout': 'breakout_strategy', 'Mean Reversion': 'mean_reversion_strategy', 'Supply & Demand': 'supply_demand_strategy', 'Momentum': 'momentum_strategy', 'Fibonacci Confluence': 'fib_confluence_strategy', 'VWAP Reversion': 'vwap_reversion_strategy', 'Options Selling (Stub)': 'options_selling_stub', 'Pullback Entry': 'pullback_entry_strategy', 'Liquidity Sweep': 'liquidity_sweep_strategy'}[strategy_name])

# Define symbols
symbols = ["BTC-USD", "ETH-USD", "BNB-USD", "XRP-USD", "SOL-USD"]

# Multi-symbol scan
results = []
for symbol in symbols:
    df = get_data(symbol)
    if not df.empty:
        try:
            if "options" in strategy_func.__name__:
                signals = pd.DataFrame([{"symbol": symbol, "note": "stubbed options logic"}])
            else:
                signals = strategy_func(df)
            if not signals.empty:
                results.append({"Symbol": symbol, "Matches": len(signals)})
        except Exception as e:
            results.append({"Symbol": symbol, "Error": str(e)})

if results:
    st.subheader("Matching Symbols")
    st.dataframe(pd.DataFrame(results))
else:
    st.info("No matching signals found for the selected strategy.")

# Chart Integration
for res in results:
    if res[\"details\"]:
        df = pd.DataFrame(res[\"details\"])
        st.dataframe(df)
        with st.expander(\"📈 View Chart\"):
            fig = plot_signal_chart(df)
            st.plotly_chart(fig, use_container_width=True)

# === Match Results with Plotly Charts ===
for res in results:
    st.markdown(f"### {res['symbol']} — Matches: {res.get('matches', 0)}")
    if res.get("details"):
        df = pd.DataFrame(res["details"])
        st.dataframe(df)

        with st.expander("📈 View Chart"):
            fig = plot_signal_chart(df)
            st.plotly_chart(fig, use_container_width=True)

# === Match Results with Plotly Charts ===
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

# === Match Results with Plotly Charts ===
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

# === Match Results with Plotly Charts ===
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

# === Match Results with Plotly Charts ===
for res in results:
    if 'error' in res:
        st.error(f"{res['symbol']}: {res['error']}")
    else:
        st.markdown(f"### {res['symbol']} — Matches: {res.get('matches', 0)}")
        if res.get('details'):
            df = pd.DataFrame(res['details'])
            st.dataframe(df)
            with st.expander('📈 View Chart'):
                fig = plot_signal_chart(df)
                st.plotly_chart(fig, use_container_width=True)

# === Match Results with Plotly Charts ===
for res in results:
    if "error" in res:
        st.error(f"{res['symbol']}: {res['error']}")
    else:
        st.markdown(f"### {res['symbol']} — Matches: {res.get('matches', 0)}")
        if res.get('details'):
            df = pd.DataFrame(res['details'])
            st.dataframe(df)

            with st.expander("📈 View Chart"):
                fig = plot_signal_chart(df)
                st.plotly_chart(fig, use_container_width=True)
