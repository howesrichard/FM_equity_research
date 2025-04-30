import pandas as pd
import matplotlib.pyplot as plt
import yfinance as yf
import os

def plot_stock_price_chart():
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
    for col in price_targets.columns:
        if col != "Date":
            price_targets = price_targets.rename(columns={col: "Target Price"})
            break
    price_targets = price_targets.sort_values("Date")

    # --- Plot 1: BEN.AX vs ASX200 (with dual y-axes) ---
    fig, ax1 = plt.subplots(figsize=(5, 5))  # Square aspect

    ax1.plot(bendigo["Close"], color='tab:blue', label="BEN.AX")
    ax1.set_ylabel("BEN.AX (AUD)", fontsize=9, color='tab:blue')
    ax1.tick_params(axis='y', labelcolor='tab:blue', labelsize=8)
    ax1.tick_params(axis='x', labelsize=8)

    ax2 = ax1.twinx()
    ax2.plot(asx200["Close"], color='tab:orange', label="ASX200", alpha=0.7)
    ax2.set_ylabel("ASX200", fontsize=9, color='tab:orange')
    ax2.tick_params(axis='y', labelcolor='tab:orange', labelsize=8)

    ax1.set_title("BEN vs ASX200", fontsize=10)
    ax1.set_xlabel("Date", fontsize=9)

    fig.tight_layout(pad=1.0)
    plt.grid(True, linewidth=0.4)
    plt.savefig("bendigo_vs_asx200.png", dpi=300)

    # --- Plot 2: BEN.AX vs Analyst Price Targets ---
    fig2, ax = plt.subplots(figsize=(5, 5))

    ax.plot(bendigo["Close"], label="BEN.AX", linewidth=1)
    ax.plot(price_targets["Date"], price_targets["Target Price"],
            color='red', label="Analyst Targets", linestyle='--', linewidth=1)

    ax.set_title("BEN vs Analyst Targets", fontsize=10)
    ax.set_xlabel("Date", fontsize=9)
    ax.set_ylabel("Price (AUD)", fontsize=9)
    ax.tick_params(labelsize=8)
    ax.legend(fontsize=8)
    ax.grid(True, linewidth=0.4)

    fig2.tight_layout(pad=1.0)
    plt.savefig("bendigo_vs_targets.png", dpi=300)

    return None

plot_stock_price_chart()