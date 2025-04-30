import pandas as pd
import matplotlib.pyplot as plt
import yfinance as yf
import os

# --- Set working directory to script location ---
script_dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(script_dir)

# --- Set date range ---
start_date = "2020-04-25"
end_date = "2025-04-25"

# --- Download stock data ---
bendigo = yf.download("BEN.AX", start=start_date, end=end_date)
asx200 = yf.download("^AXJO", start=start_date, end=end_date)

# --- Load and prepare historical price target CSV ---
price_targets = pd.read_csv("Historical_Price_Targets.csv", parse_dates=["Date"])

# Rename the price target column automatically (first non-date column)
for col in price_targets.columns:
    if col != "Date":
        price_targets = price_targets.rename(columns={col: "Target Price"})
        break

price_targets = price_targets.sort_values("Date")

# --- Plot 1: BEN.AX vs ASX200 (with dual y-axes) ---
fig, ax1 = plt.subplots(figsize=(12, 6))

# Left Y-axis: BEN.AX
ax1.plot(bendigo["Close"], color='tab:blue', label="BEN.AX (Bendigo Bank)")
ax1.set_ylabel("Bendigo Bank Price (AUD)", color='tab:blue')
ax1.tick_params(axis='y', labelcolor='tab:blue')

# Right Y-axis: ASX200
ax2 = ax1.twinx()
ax2.plot(asx200["Close"], color='tab:orange', label="ASX200 (^AXJO)", alpha=0.7)
ax2.set_ylabel("ASX200 Index Level", color='tab:orange')
ax2.tick_params(axis='y', labelcolor='tab:orange')

# Title and formatting
plt.title("Bendigo Bank vs ASX200 Index (Dual Y-Axis)")
ax1.set_xlabel("Date")
fig.tight_layout()
plt.grid(True)

# --- Save Plot 1 ---
plt.savefig("bendigo_vs_asx200.png", dpi=300)


# --- Plot 2: BEN.AX vs Historical Analyst Price Targets ---
plt.figure(figsize=(12, 6))
plt.plot(bendigo["Close"], label="BEN.AX Actual Price")
plt.plot(price_targets["Date"], price_targets["Target Price"],
         color='red', label="Analyst Price Targets", linestyle='--')
plt.title("Bendigo Bank vs Historical Analyst Price Targets")
plt.xlabel("Date")
plt.ylabel("Price (AUD)")
plt.legend()
plt.grid(True)
plt.tight_layout()

# --- Save Plot 2 ---
plt.savefig("bendigo_vs_targets.png", dpi=300)

