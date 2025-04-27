# Key ratios and financial metric calculation functions

###############################################################################################
# Section 1: Functions to obtain the key ratios and metrics required for the financial summary 

# Function to calculate the net profit margin of a stock
def calculate_net_profit_margin(net_income, revenue):
    return net_income / revenue

# Function to calculate the earnings per share (EPS) of a stock
def calculate_eps(net_income, shares_outstanding):
    return net_income / shares_outstanding

# Function to calculate the P/E ratio of a stock
def calculate_pe_ratio(price, earnings):
    return price / earnings

# Function to calculate the dividends per share (DPS) of a stock
def calculate_dividends_per_share(dividends_paid, shares_outstanding):
    return dividends_paid / shares_outstanding

# Function to calculate the dividend payout ratio (DPR) of a stock
def calculate_dividend_payout_ratio(dividends_paid, net_income):
    return dividends_paid / net_income

# Function to calculate the return on equity (ROE) of a stock
def calculate_roe(net_income, shareholders_equity):
    return net_income / shareholders_equity

# Function to calculate return on assets (ROA) of a stock
def calculate_roa(net_income, total_assets):
    return net_income / total_assets

# Function to calculate return on investmed capital (ROIC) of a stock
def calculate_roic(net_income, invested_capital):
    return net_income / invested_capital

###############################################################################################
# Section 2: Functions obtain the key ratios and metrics required for the ratio analysis 

##### Leverage Ratios #####
# Function to calculate the interest burden ratio of a stock
def calculate_interest_burden_ratio(ebit, interest_expense):
    return (ebit - interest_expense) / ebit

# Function to calculate the interest coverage ratio of a stock 
def calculate_interest_coverage_ratio(ebit, interest_expense):
    return ebit / interest_expense

# Function to calculate the leverage ratio of a stock
def calculate_leverage_ratio(total_assets, total_equity):
    return total_assets / total_equity

# Function to calculate the compound leverage factor of a stock

##### Asset Utilisation Ratios #####
# Function to calculate the asset turnover ratio of a stock
def calculate_asset_turnover_ratio(revenue, total_assets):
    return revenue / total_assets

# Function to calculate the fixed asset turnover ratio of a stock
def calculate_fixed_asset_turnover_ratio(revenue, net_fixed_assets):
    return revenue / net_fixed_assets

# Function to calculate the inventory turnover ratio of a stock
def calculate_inventory_turnover_ratio(cost_of_goods_sold, average_inventory):
    return cost_of_goods_sold / average_inventory

# Function to calculate the receivables turnover ratio of a stock
def calculate_receivables_turnover_ratio(revenue, average_accounts_receivable):
    return revenue / average_accounts_receivable

# Function to calculate the payables turnover ratio of a stock
def calculate_payables_turnover_ratio(cost_of_goods_sold, average_accounts_payable):
    return cost_of_goods_sold / average_accounts_payable

##### Liquidity Ratios #####
# Function to calculate the current ratio of a stock
def calculate_current_ratio(current_assets, current_liabilities):
    return current_assets / current_liabilities

# Function to calculate the quick ratio of a stock 
def calculate_quick_ratio(current_assets, current_liabilities, inventory):
    return (current_assets - inventory) / current_liabilities

# Function to calculate the cash ratio of a stock
def calculate_cash_ratio(cash_and_cash_equivalents, current_liabilities):
    return cash_and_cash_equivalents / current_liabilities

##### Profitability Ratios #####
# NOTE: These ratios, including net profit margin, ROA, ROE & ROIC, are already defined in Section 1

##### Margin Ratios #####
# NOTE: Net profit margin is already defined in Section 1

# Function to calculate the gross profit margin 
def calculate_gross_profit_margin(gross_profit, revenue):
    return gross_profit / revenue

# Function to calculate the EBITDA margin 
def calculate_ebitda_margin(ebitda, revenue):
    return ebitda / revenue

# Function to calculate the EBIT margin 
def calculate_ebit_margin(ebit, revenue):
    return ebit / revenue

# Print a message indicating that the script is running
print("Script is running!")
