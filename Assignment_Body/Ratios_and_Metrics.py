import yfinance as yf

def get_financial_ratios(ticker: str):
    stock = yf.Ticker(ticker)
    info = stock.info

    print(f"Financial Ratios for {ticker}:\n")
    
    ratios = {
        "Price to Earnings (P/E)": info.get("trailingPE"),
        "Forward P/E": info.get("forwardPE"),
        "Price to Book (P/B)": info.get("priceToBook"),
        "Return on Assets (ROA)": info.get("returnOnAssets"),
        "Return on Equity (ROE)": info.get("returnOnEquity"),
        "Profit Margin": info.get("profitMargins"),
        "Operating Margin": info.get("operatingMargins"),
        "Gross Margins": info.get("grossMargins"),
        "EBITDA Margins": info.get("ebitdaMargins"),
        "Revenue Growth": info.get("revenueGrowth"),
        "Earnings Growth": info.get("earningsGrowth"),
        "Dividend Yield": info.get("dividendYield"),
        "Beta": info.get("beta"),
    }

    for key, value in ratios.items():
        if value is not None:
            print(f"{key}: {value:.4f}")
        else:
            print(f"{key}: Data not available")

if __name__ == "__main__":
    get_financial_ratios("BEN.AX")