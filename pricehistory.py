import matplotlib.pyplot as plt
import yfinance as yf

def generate_stock_plot(ticker, start_date, end_date, output_filename):

    # Download the stock data using yfinance API
    data = yf.download(ticker, start=start_date, end=end_date)
    
    if data.empty:
        raise ValueError(f"No data found for ticker: {ticker}")
    
    # Create a new figure and axis for plotting
    fig, ax = plt.subplots(figsize=(10, 5))
    
    # Plot the closing price history
    ax.plot(data.index, data['Close'], label='Close Price')
    ax.set_title(f"{ticker} Price History")
    ax.set_xlabel("Date")
    ax.set_ylabel("Price")
    ax.legend()
    
    return fig