import yfinance as yf
import matplotlib.pyplot as plt

# download Bendigo data
Bendigo = yf.download(
    tickers='BEN.AX', 
    start='2020-04-27', 
    end='2025-04-27'
)

# download ASX data
ASX = yf.download(
    tickers='ASX.AX', 
    start='2020-04-27', 
    end='2025-04-27'
)

# create a figure and axis
fig, ax1 = plt.subplots(figsize=(10,6))

# plot Bendigo on the first axis
ax1.plot(Bendigo['Close'], label='Bendigo Close Price', color='blue')
ax1.set_xlabel('Date')
ax1.set_ylabel('Bendigo Price (AUD)', color='blue')
ax1.tick_params(axis='y', labelcolor='blue')

# makes a second axis that shares the same x-axis
ax2 = ax1.twinx()

# plot ASX on the second axis
ax2.plot(ASX['Close'], label='ASX Close Price', color='green')
ax2.set_ylabel('ASX Price (AUD)', color='green')
ax2.tick_params(axis='y', labelcolor='green')

# adding title
plt.title('Bendigo vs ASX Closing Prices')

# show the plot
plt.show()
