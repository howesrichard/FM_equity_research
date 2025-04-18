def calculate_pe_ratio(price, earnings_per_share):
    """
    Price-to-Earnings (P/E) Ratio = Share Price / Earnings Per Share
    """
    try:
        return round(price / earnings_per_share, 2)
    except ZeroDivisionError:
        return None

def calculate_roe(net_income, shareholder_equity):
    """
    Return on Equity (ROE) = Net Income / Shareholder Equity
    """
    try:
        return round(net_income / shareholder_equity, 2)
    except ZeroDivisionError:
        return None

def calculate_ebitda_margin(ebitda, revenue):
    """
    EBITDA Margin = EBITDA / Revenue
    """
    try:
        return round(ebitda / revenue, 2)
    except ZeroDivisionError:
        return None
