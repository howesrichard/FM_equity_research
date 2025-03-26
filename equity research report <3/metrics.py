# metrics.py

def calculate_pe_ratio(market_cap, net_income):
    try:
        return round(market_cap / net_income, 2)
    except:
        return None

def calculate_roe(net_income, total_equity):
    try:
        return round((net_income / total_equity) * 100, 2)
    except:
        return None

def calculate_current_ratio(current_assets, current_liabilities):
    try:
        return round(current_assets / current_liabilities, 2)
    except:
        return None

def calculate_debt_to_equity(total_debt, total_equity):
    try:
        return round(total_debt / total_equity, 2)
    except:
        return None

def calculate_net_profit_margin(net_income, revenue):
    try:
        return round((net_income / revenue) * 100, 2)
    except:
        return None
