
# Trading Strategies Scanner - Setup & Deployment Walkthrough

## 1. Project Overview
This project scans top cryptocurrencies using 10 widely accepted profitable trading strategies. It includes:
- Python strategy scripts  
- Streamlit dashboard  
- GitHub-friendly structure  
- Render.com deployment config  

## 2. Folder Structure
```
Root Folder:
- .streamlit/config.toml (theme)
- data/symbols.json
- notebooks/ (for testing)
- src/strategies/ (all 10 strategies)
- src/utils/ (data fetching, backtesting)
- app.py (Streamlit UI)
- requirements.txt
- deployment/render.yaml
```

## 3. Strategy Modules
Each strategy file inside `src/strategies/` returns a filtered DataFrame of valid trade signals.  
Examples include:
- trend_following.py  
- breakout.py  
- mean_reversion.py  
... up to liquidity_sweep.py

## 4. How to Run Locally
1. Clone the repo  
2. Create a virtual environment  
3. Run: `pip install -r requirements.txt`  
4. Launch app: `streamlit run app.py`

## 5. Deploy on Render
1. Push your project to GitHub  
2. Go to [render.com](https://render.com) and create a new Web Service  
3. Link your GitHub repo  
4. Use `render.yaml` for build/start commands:  
   - Build: `pip install -r requirements.txt`  
   - Start: `streamlit run app.py`  
5. Render deploys your dashboard live

## 6. Customization Tips
- Add more strategies to `src/strategies/`  
- Enhance visuals in `app.py`  
- Use Telegram API or Discord bots to send alerts  
- Implement full backtesting with `src/utils/backtester.py`

## 7. Contact & Branding
Project created for Financial Literacy TV.  
For help or extensions, contact Ian or your trading tech partner.
