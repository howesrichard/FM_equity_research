
def get_financial_metrics(Ticker: str):
    """
    Fetches financial metrics for a given stock ticker using yfinance.

    Args:
        Ticker (str): The stock ticker symbol.

    Returns:
        dict: A dictionary containing financial metrics.
    """

    import yfinance as yf

    # Fetch the stock data
    stock = yf.Ticker(Ticker)
    
    # Get financial metrics
    info = stock.info
    metrics = {
        "current_price": info.get("currentPrice"),
        "market_cap": info.get("marketCap"),
        "P/E Ratio": info.get("forwardPE"),
        "dividend_yield": info.get("dividendYield"),
        "Debt to Equity": info.get("debtToEquity"),
        "Return on Equity": info.get("returnOnEquity"),
        "Operating Margin": info.get("operatingMargins"),
        "Profit Margin": info.get("profitMargins"),
        "Revenue": info.get("totalRevenue"),
        "Gross Profit": info.get("grossProfits"),
        "Operating Income": info.get("operatingIncome"),
        "Net Income": info.get("netIncome"),
    }
    return metrics