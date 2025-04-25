import matplotlib.pyplot as plt
import yfinance as yf

# # Function to calculate the P/E ratio of a stock
# def calculate_pe_ratio(price, earnings):
#     return price / earnings

# # Function to calculate the earnings per share of a stock
# def calculate_eps(net_income, shares_outstanding):
#     return net_income / shares_outstanding

# # Function to calculate ROA of a stock
# def calculate_roa(net_income, total_assets):
#     return net_income / total_assets

# Take user input for ticker
TICKER = input('Enter a stock ticker (e.g. BHP.AX): ').upper()

stock = yf.Ticker(TICKER)
stock_prices = stock.history(period="10y")


def plot_stock(ticker, save_path='stock_plot.png'):
    stock = yf.Ticker(ticker)
    stock_prices = stock.history(period="10y")

    plt.figure(figsize=(10, 5))
    plt.plot(stock_prices['Close'])
    plt.title(f"{ticker} Stock Prices")
    plt.xlabel("Date")
    plt.ylabel("Price")
    plt.tight_layout()

    # Save the plot as an image
    plt.savefig(save_path)
    plt.close()  # Close the figure to avoid displaying it in Jupyter




# try:
#     # Get stock information
#     stock = yf.Ticker(TICKER)
#     stock_prices = stock.history(period="10y")
#     stock_info = stock.info
#     stock_financials = stock.financials
#     stock_balance_sheet = stock.balance_sheet

#     # Extract relevant information
#     last_price = stock_prices['Close'].iloc[-1]
#     earnings = stock_financials.loc["Net Income"].iloc[0]
#     dividend = stock_info['lastDividendValue']
#     shares_outstanding = stock_info['sharesOutstanding']
#     total_assets = (stock_balance_sheet.loc["Total Assets"].iloc[0] + stock_balance_sheet.loc["Total Assets"].iloc[1]) / 2

#     def calculate_dividend_yield(dividend, price):
#         return dividend / price

#     dividend_yield = calculate_dividend_yield(dividend, last_price) * 100
#     eps = calculate_eps(earnings, shares_outstanding)
#     pe_ratio = calculate_pe_ratio(last_price, eps)
#     roa = calculate_roa(earnings, total_assets) * 100

# except Exception as e:
#     print(f"Error: {e}")

# print(f"Chosen Stock: {TICKER} \nLast Share Price: {last_price:.2f} \nPE Ratio: {pe_ratio:.2f} \nDividend Yield: {dividend_yield:.2f}% \nEPS: {eps:.2f} \nROA: {roa:.2f}%")