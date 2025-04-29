import yfinance as yf

def financial_metrics_bendigo():
    ticker = "BEN.AX"
    stock = yf.Ticker(ticker)
    stock_prices = stock.history(period="1y")
    stock_info = stock.info
    stock_financials = stock.financials
    stock_balance_sheet = stock.balance_sheet
    stock_cashflow = stock.cashflow

    try:
        # Extract common data
        last_price = stock_prices['Close'].iloc[-1]
        earnings = stock_financials.loc["Net Income"].iloc[0]
        revenue = stock_financials.loc["Total Revenue"].iloc[0] if "Total Revenue" in stock_financials.index else 0
        operating_income = stock_financials.loc["Operating Income"].iloc[0] if "Operating Income" in stock_financials.index else None

        shares_outstanding = stock_info.get("sharesOutstanding", 0)
        book_value_per_share = stock_info.get("bookValue", 0)
        dividend_per_share = stock_info.get("lastDividendValue", 0) or 0

        # Dividend fallback: use forward dividend yield * price if missing
        if not dividend_per_share and stock_info.get("dividendYield"):
            dividend_per_share = stock_info["dividendYield"] * last_price

        # Dividends Paid fallback
        try:
            dividends_paid = abs(stock_cashflow.loc["Dividends Paid"].iloc[0])
        except:
            dividends_paid = dividend_per_share * shares_outstanding if dividend_per_share and shares_outstanding else 0

        # Total assets (2-year avg if possible)
        total_assets = 0
        if "Total Assets" in stock_balance_sheet.index:
            total_assets_row = stock_balance_sheet.loc["Total Assets"]
            total_assets = total_assets_row.iloc[:2].mean() if total_assets_row.shape[0] >= 2 else total_assets_row.iloc[0]

        # Equity fallback: use book value × shares
        if "Total Stockholder Equity" in stock_balance_sheet.index:
            total_equity_row = stock_balance_sheet.loc["Total Stockholder Equity"]
            total_equity = total_equity_row.iloc[:2].mean() if total_equity_row.shape[0] >= 2 else total_equity_row.iloc[0]
        else:
            total_equity = book_value_per_share * shares_outstanding

        # --- Ratio Calculations ---
        eps = earnings / shares_outstanding if shares_outstanding else 0
        pe_ratio = last_price / eps if eps else 0
        dividend_yield = (dividend_per_share / last_price) * 100 if last_price else 0
        payout_ratio = (dividends_paid / earnings) * 100 if earnings else 0
        roa = (earnings / total_assets) * 100 if total_assets else 0
        roe = (earnings / total_equity) * 100 if total_equity else 0
        profit_margin = (earnings / revenue) * 100 if revenue else 0
        operating_margin = (operating_income / revenue * 100) if operating_income and revenue else stock_info.get("operatingMargins", 0) * 100 if stock_info.get("operatingMargins") else 0
        pb_ratio = last_price / book_value_per_share if book_value_per_share else 0

        return {
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

    except Exception as e:
        print("Error calculating financial metrics:", e)
        return None

# --- Run and Display ---
if __name__ == "__main__":
    metrics = financial_metrics_bendigo()

    if metrics:
        print("\n--- Financial Ratios for Bendigo Bank (BEN.AX) ---")
        for key, value in metrics.items():
            print(f"{key}: {value}")
    else:
        print("Could not fetch financials.")
