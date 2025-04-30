import yfinance as yf 
import pandas as pd

# This function fetches and calculates financial metrics for Bendigo 
def financial_metrics_bendigo():
    ticker = "BEN.AX"
    stock = yf.Ticker(ticker)

    # Download historical stock prices, general info, and financial statements
    stock_prices = stock.history(period="1y")
    stock_info = stock.info
    stock_financials = stock.financials
    stock_balance_sheet = stock.balance_sheet
    stock_cashflow = stock.cashflow

    try:
        # Get the most recent closing price
        last_price = stock_prices['Close'].iloc[-1]
        
        # Extract net income and revenue
        earnings = stock_financials.loc["Net Income"].iloc[0]
        revenue = stock_financials.loc["Total Revenue"].iloc[0] if "Total Revenue" in stock_financials.index else 0
        operating_income = stock_financials.loc["Operating Income"].iloc[0] if "Operating Income" in stock_financials.index else None

        # Get number of shares, book value per share, and last dividend per share
        shares_outstanding = stock_info.get("sharesOutstanding", 0)
        book_value_per_share = stock_info.get("bookValue", 0)
        dividend_per_share = stock_info.get("lastDividendValue", 0) or 0

        # If dividend per share is not available, estimate it using dividend yield
        if not dividend_per_share and stock_info.get("dividendYield"):
            dividend_per_share = stock_info["dividendYield"] * last_price

        # Get total amount of dividends paid from the cash flow statement
        try:
            dividends_paid = abs(stock_cashflow.loc["Dividends Paid"].iloc[0])
        except:
            # If not available, estimate using dividend per share times number of shares
            dividends_paid = dividend_per_share * shares_outstanding if dividend_per_share and shares_outstanding else 0

        # Compute total assets by taking the average of the last two periods if possible
        total_assets = 0
        if "Total Assets" in stock_balance_sheet.index:
            total_assets_row = stock_balance_sheet.loc["Total Assets"]
            total_assets = total_assets_row.iloc[:2].mean() if total_assets_row.shape[0] >= 2 else total_assets_row.iloc[0]

        # Compute total equity similarly or fallback to book value times number of shares
        if "Total Stockholder Equity" in stock_balance_sheet.index:
            total_equity_row = stock_balance_sheet.loc["Total Stockholder Equity"]
            total_equity = total_equity_row.iloc[:2].mean() if total_equity_row.shape[0] >= 2 else total_equity_row.iloc[0]
        else:
            total_equity = book_value_per_share * shares_outstanding

        # Begin calculating financial ratios

        # Earnings per share
        eps = earnings / shares_outstanding if shares_outstanding else 0

        # Price to earnings ratio
        pe_ratio = last_price / eps if eps else 0

        # Dividend yield as a percentage
        dividend_yield = (dividend_per_share / last_price) * 100 if last_price else 0

        # Payout ratio: dividends paid as a percentage of earnings
        payout_ratio = (dividends_paid / earnings) * 100 if earnings else 0

        # Return on assets
        roa = (earnings / total_assets) * 100 if total_assets else 0

        # Return on equity
        roe = (earnings / total_equity) * 100 if total_equity else 0

        # Profit margin
        profit_margin = (earnings / revenue) * 100 if revenue else 0

        # Operating margin, fallback to reported margin if not calculable
        operating_margin = (operating_income / revenue * 100) if operating_income and revenue else stock_info.get("operatingMargins", 0) * 100 if stock_info.get("operatingMargins") else 0

        # Price to book ratio
        pb_ratio = last_price / book_value_per_share if book_value_per_share else 0

        # Store all metrics in a dictionary with formatted values
        dict = {
            "Dividend Yield (%)": round(dividend_yield, 2),
            "Earnings Per Share (EPS)": round(eps, 2),
            "Price to Earnings (P/E)": round(pe_ratio, 2),
            "Return on Assets (ROA %)": round(roa, 2),
            "Return on Equity (ROE %)": round(roe, 2),
            "Profit Margin (%)": round(profit_margin, 2),
            "Operating Margin (%)": round(operating_margin, 2),
            "Price to Book (P/B)": round(pb_ratio, 2),
            "Dividend Payout Ratio (%)": round(payout_ratio, 2)
        }

        # Print to console and return as a DataFrame for further use
        print(dict)
        return pd.DataFrame(list(dict.items()), columns=['Metric', 'Value'])

    except Exception as e:
        # If anything goes wrong, print the error and return nothing
        print("Error calculating financial metrics:", e)
        return None

# Run the function if the script is executed directly
if __name__ == "__main__":
    metrics = financial_metrics_bendigo()

    # If data was fetched successfully, print it
    if metrics is not None:
        print("\n--- Financial Ratios for Bendigo Bank (BEN.AX) ---")
        print(metrics)
    else:
        print("Could not fetch financials.")
