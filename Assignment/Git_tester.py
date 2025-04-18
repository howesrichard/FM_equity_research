import pandas as pd
def net_interest_margin(net_interest, earning_assets):
    nim = net_interest / earning_assets
    return nim
def calculate_dividend_yield(dividend, last_price):
    if last_price == 0:
        return 0
    return dividend / last_price
def pe_ratio(last_price, eps):
    if eps == 0:
        return 0
    return last_price / eps
def calculate_eps(earnings, shares_outstanding):
    if shares_outstanding == 0:
        return 0
    return earnings / shares_outstanding
def calculate_roa(earnings, total_assets):
    if total_assets == 0:
        return 0
    return earnings / total_assets
def calculate_pe_ratio(last_price, eps):
    if eps == 0:
        return 0
    return last_price / eps
def calculate_eps(earnings, shares_outstanding):
    if shares_outstanding == 0:
        return 0
    return earnings / shares_outstanding




# Dividends of Bendigo and Adelaide Bank (B&A website required authentication)
url = "https://www.intelligentinvestor.com.au/shares/asx-ben/bendigo-and-adelaide-bank-limited/financials"
tables = pd.read_html(url)
df = tables[0]
print(df.head())


# yfinance stock price graph
import yfinance as yf

# Take user input for ticker
TICKER = "BEN"

try:
    # Get stock information
    stock = yf.Ticker(TICKER)
    stock_prices = stock.history(period="10y")
    stock_info = stock.info
    stock_financials = stock.financials
    stock_balance_sheet = stock.balance_sheet

    # Extract relevant information
    last_price = stock_prices['Close'].iloc[-1]
    earnings = stock_financials.loc["Net Income"].iloc[0]
    dividend = stock_info['lastDividendValue']
    shares_outstanding = stock_info['sharesOutstanding']
    total_assets = (stock_balance_sheet.loc["Total Assets"].iloc[0] + stock_balance_sheet.loc["Total Assets"].iloc[1]) / 2

    dividend_yield = calculate_dividend_yield(dividend, last_price) * 100
    eps = calculate_eps(earnings, shares_outstanding)
    pe_ratio = calculate_pe_ratio(last_price, eps)
    roa = calculate_roa(earnings, total_assets) * 100

except Exception as e:
    print(f"Error: {e}")

print(f"Chosen Stock: {TICKER} \nLast Share Price: {last_price:.2f} \nPE Ratio: {pe_ratio:.2f} \nDividend Yield: {dividend_yield:.2f}% \nEPS: {eps:.2f} \nROA: {roa:.2f}%")