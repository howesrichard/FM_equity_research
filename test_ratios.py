from financial_functions import calculate_pe_ratio, calculate_roe, calculate_ebitda_margin

print("P/E Ratio:", calculate_pe_ratio(14.50, 1.32))
print("ROE:", calculate_roe(250_000_000, 2_100_000_000))
print("EBITDA Margin:", calculate_ebitda_margin(720_000_000, 2_800_000_000))
