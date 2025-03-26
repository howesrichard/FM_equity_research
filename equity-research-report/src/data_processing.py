def fetch_financial_data(api_url, company_code):
    import requests

    response = requests.get(f"{api_url}/{company_code}")
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception("Error fetching financial data")

def compute_ratios(financial_data):
    ratios = {}
    ratios['P/E'] = financial_data['price'] / financial_data['earnings_per_share']
    ratios['Debt/Equity'] = financial_data['total_debt'] / financial_data['shareholder_equity']
    ratios['Current Ratio'] = financial_data['current_assets'] / financial_data['current_liabilities']
    return ratios