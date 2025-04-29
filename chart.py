# Import necessary libraries
import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

# Step 1: Retrieve HUB24 and ASX200 historical price data from Yahoo Finance
def fetch_price_data(ticker, start_date, end_date): # originally fetch_price_data
    historical_prices = yf.download(ticker, start=start_date, end=end_date) #originally stock_data
    return historical_prices['Close']

# HUB24 (ASX: HUB) and ASX200 (^AXJO) tickers
hub24_ticker = "HUB.AX"
asx200_ticker = "^AXJO"

# Define date range
start_date = "2020-05-05"
end_date = "2025-04-29"

# Fetch data
hub24_prices = fetch_price_data(hub24_ticker, start_date, end_date)
asx200_prices = fetch_price_data(asx200_ticker, start_date, end_date)

# # Step 2: Load historical price targets from CSV
price_targets = "price_targets.csv"  # Replace with your actual file path
price_targets = pd.read_csv(price_targets, parse_dates=["Date"]) # this command will read the csv file and parse the date column, parse means to convert the date column to datetime format
price_targets.set_index("Date", inplace=True) # set the date column as index, indexing means to set the date column as the index of the dataframe 
# #what is the index of a dataframe? The index of a dataframe is the label for each row, it is used to identify each row uniquely. In this case, the date column is used as the index to identify each row uniquely.

# Step 3: Plot the data with two y-axes
fig, ax1 = plt.subplots(figsize=(12, 6))

# Plot ASX200 price history on the primary y-axis
asx200_price = ax1.plot(asx200_prices, label="ASX200 Index", color="orange")
ax1.set_xlabel("Date")
ax1.set_ylabel("ASX200 Price (AUD)", color="orange")
ax1.tick_params(axis='y', labelcolor="orange")
ax1.grid()

# Create a secondary y-axis for HUB24 prices
ax2 = ax1.twinx()

# Plot HUB24 Price history on secondary y-axis
hub24_price = ax2.plot(hub24_prices, label="HUB24 Price History", color="blue")
ax2.set_ylabel("HUB24 Price (AUD)", color="blue")
ax2.tick_params(axis='y', labelcolor="blue")

# Plot HUB24 price targets on secondary y-axis
price_targets = ax2.plot(price_targets.index, price_targets['12M Tgt. Price'], label="HUB24 Price Targets", color="red", linestyle="--")

# Add a title
plt.title("HUB24 and ASX200 Price History")
fig.tight_layout()

# Adding legend for three graphs
custom_labels = ["ASX200 Price History", "HUB24 Price History", "HUB24 Price Targets"]
lines = [asx200_price[0], hub24_price[0], price_targets[0]] # both variables are lists of lines due to plot() function's nature, hence [0] is used to retrieve the line object within the lists
ax1.legend(lines, custom_labels, loc="upper left")

# Save and show the chart
chart = "hub24_asx200_dual_axis_chart.png" #
plt.savefig(chart) 
print(chart)