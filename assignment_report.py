from financial_ratios import get_financial_metrics

TICKER = "AAPL"

data = get_financial_metrics(TICKER)
print(data)