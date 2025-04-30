import pandas as pd
import matplotlib.pyplot as plt
import yfinance as yf
import os 
# Set date range
start_date = "2020-04-27"
end_date = "2025-04-27"

# Download stock data
bendigo = yf.download("BEN.AX", start=start_date, end=end_date)
asx200 = yf.download("^AXJO", start=start_date, end=end_date)

# Load CSV (Date + Daily Target Price (CIQ))
os.chdir("FM_equity_research")
price_targets = pd.read_csv("Updated_HPT.csv", parse_dates= ["date"], index_col='date')
price_targets = price_targets.rename(columns={"Daily Target Price (CIQ)": "Target Price"})
price_targets = price_targets.sort_values("Date")

# Plot 1: BEN.AX vs ASX200
plt.figure(figsize=(12, 6))
plt.plot(bendigo["Close"], label="BEN.AX (Bendigo Bank)")
plt.plot(asx200["Close"], label="ASX200 (^AXJO)", alpha=0.7)
plt.title("Bendigo Bank vs ASX200 Index")
plt.xlabel("Date")
plt.ylabel("Closing Price (AUD)")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

# Plot 2: BEN.AX vs Historical Price Targets
plt.figure(figsize=(12, 6))
plt.plot(bendigo["Close"], label="BEN.AX Actual Price")
plt.scatter(price_targets["Date"], price_targets["Target Price"], color='red', label="Historical Price Targets", zorder=5)
plt.title("Bendigo Bank vs Historical Analyst Price Targets")
plt.xlabel("Date")
plt.ylabel("Price (AUD)")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

