import pandas as pd
import matplotlib.pyplot as plt
import yfinance as yf
import os

# This function generates two stock price charts and saves them as PNG images
def plot_stock_price_chart():
    # Set the working directory to the folder where this script is
    script_dir = os.path.dirname(os.path.abspath(__file__))
    os.chdir(script_dir)

    # Define the date range for the charts
    start_date = "2020-04-25"
    end_date = "2025-04-25"

    # Download daily price data for Bendigo and the ASX200
    bendigo = yf.download("BEN.AX", start=start_date, end=end_date)
    asx200 = yf.download("^AXJO", start=start_date, end=end_date)

    # Load the CSV file with historical analyst price targets (5Y)
    price_targets = pd.read_csv("Historical_Price_Targets.csv", parse_dates=["Date"])

    # Rename the column with target prices to a standard name "Target Price"
    for col in price_targets.columns:
        if col != "Date":
            price_targets = price_targets.rename(columns={col: "Target Price"})
            break

    # Sort the CSV by date to ensure the line chart is smooth
    price_targets = price_targets.sort_values("Date")

    # Chart 1: Bendigo Bank vs ASX200:

    # Create a chart with two Y axes: one for Bendigo and one for the ASX200
    fig, ax1 = plt.subplots(figsize=(5, 5))  # Make the plot square

    # Plot Bendigo Bank share price
    ax1.plot(bendigo["Close"], color='tab:blue', label="BEN.AX")
    ax1.set_ylabel("BEN.AX (AUD)", fontsize=9, color='tab:blue')
    ax1.tick_params(axis='y', labelcolor='tab:blue', labelsize=8)
    ax1.tick_params(axis='x', labelsize=8)

    # Create a second Y axis for the ASX200 index
    ax2 = ax1.twinx()
    ax2.plot(asx200["Close"], color='tab:orange', label="ASX200", alpha=0.7)
    ax2.set_ylabel("ASX200", fontsize=9, color='tab:orange')
    ax2.tick_params(axis='y', labelcolor='tab:orange', labelsize=8)

    # Add title and axis labels
    ax1.set_title("BEN vs ASX200", fontsize=10)
    ax1.set_xlabel("Date", fontsize=9)

    # Tidy layout and save to file
    fig.tight_layout(pad=1.0)
    plt.grid(True, linewidth=0.4)
    plt.savefig("bendigo_vs_asx200.png", dpi=300)  # Save as high-quality PNG

    #Chart 2: Bendigo vs Analyst Price Targets

    # Create a second chart comparing BEN price with analyst expectations
    fig2, ax = plt.subplots(figsize=(5, 5))

    # Plot Bendigo share price
    ax.plot(bendigo["Close"], label="BEN.AX", linewidth=1)

    # Plot analyst target prices as a dashed red line
    ax.plot(price_targets["Date"], price_targets["Target Price"],
            color='red', label="Analyst Targets", linestyle='--', linewidth=1)

    # Add title and axis formatting
    ax.set_title("BEN vs Analyst Targets", fontsize=10)
    ax.set_xlabel("Date", fontsize=9)
    ax.set_ylabel("Price (AUD)", fontsize=9)
    ax.tick_params(labelsize=8)
    ax.legend(fontsize=8)
    ax.grid(True, linewidth=0.4)

    # Save the second chart
    fig2.tight_layout(pad=1.0)
    plt.savefig("bendigo_vs_targets.png", dpi=300)

# Run the function to generate the plots
plot_stock_price_chart()
