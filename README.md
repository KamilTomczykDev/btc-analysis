# 📊 Crypto Dashboard – ETL with API Integration and Historical BTC Comparison

This project simulates a real-world data engineering workflow using Python. It extracts live cryptocurrency data from the CoinGecko API and combines it with historical Bitcoin prices from 2018. The final result is presented in an interactive dashboard built with Streamlit.

---

## 🚀 Project Overview

### ✅ Main Features:

- Fetches **live data** for top cryptocurrencies using the CoinGecko API
- Loads **historical BTC prices** (from CSV) and compares them with current data
- Cleans and transforms both datasets
- Stores data in a **SQLite** database
- Visualizes everything in a **Streamlit dashboard**

---

## 🔧 Technologies Used

- **Python 3.12**
- **pandas** – Data manipulation
- **requests** – API integration
- **sqlite3 / SQLAlchemy** – Data storage
- **Streamlit** – Interactive dashboard
- **plotly** – Charting
- **Git** - Version control

---

## 📥 Data Sources

- **[CoinGecko API](https://www.coingecko.com/en/api)** – live crypto data
- **CSV File** – simulated historical BTC prices for 2018 (in `data/raw/historical_btc_2018.csv`)

---

## 🧪 How to Run the Project

### 1. Clone the repository

```bash
git clone https://github.com/your-username/crypto-etl-dashboard.git
cd crypto-etl-dashboard
```

### 2. Create a virtual environment (optional but recommended)

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\\Scripts\\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the ETL pipeline

```bash
python run_etl.py
```

This will:

- Fetch current coin data from the CoinGecko API
- Load historical BTC data from CSV
- Clean and store data into a local SQLite database

### 5. Run the Streamlit dashboard

```bash
streamlit run dashboard/app.py
```

Then open the dashboard in your browser (usually: http://localhost:8501)

---

## 📸 Screenshots

_(Add screenshots of your dashboard here, e.g. table view, BTC chart, price changes)_

---

## 🌐 Deployment (optional)

You can deploy the Streamlit app for free using:

- [Streamlit Cloud](https://streamlit.io/cloud)
- [Render](https://render.com)
- [Heroku](https://heroku.com)

---

## 📌 Project Status

✅ Completed core features  
🔜 Optional improvements: data scheduling, more APIs, deployment

---

## 🙋‍♂️ Author

**Kamil [YourLastName]**  
Junior Data Engineer | Python & SQL enthusiast
