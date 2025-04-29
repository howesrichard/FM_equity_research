import pandas as pd
import os

# Relative path
current_dir = os.path.dirname(__file__)
file_path = os.path.join(current_dir, 'BENDIGO.xlsx')

# Load Excel
df = pd.read_excel(file_path, sheet_name='Dividend Discount Model', header=None)

# --- Read correct inputs ---

# Cost of Equity from J12 (Row 11, Column 9)
cost_of_equity = float(df.iloc[11, 9])

# Terminal Growth Rate from J13 (Row 12, Column 9)
terminal_growth = float(df.iloc[12, 9])

# Convert to decimal if needed
cost_of_equity = cost_of_equity / 100 if cost_of_equity > 1 else cost_of_equity
terminal_growth = terminal_growth / 100 if terminal_growth > 1 else terminal_growth

# Dividends Per Share (DPS) N31–R31
dps = df.iloc[30, 13:18].astype(float).values

# Years Away N34–R34
years_away = df.iloc[33, 13:18].astype(float).values

# Terminal Year DPS (J42)
terminal_dps = float(df.iloc[41, 9])

# Terminal Years Away (J46)
terminal_years_away = float(df.iloc[45, 9])

# --- Perform DDM Calculations ---

# Discounted Dividends
discounted_dividends = dps / (1 + cost_of_equity) ** years_away
present_value_dividends = discounted_dividends.sum()

# Terminal Value
terminal_value = (terminal_dps * (1 + terminal_growth)) / (cost_of_equity - terminal_growth)

# Discounted Terminal Value
discounted_terminal_value = terminal_value / (1 + cost_of_equity) ** terminal_years_away

# Total Intrinsic Value
intrinsic_value = present_value_dividends + discounted_terminal_value

# --- Print everything (rounded nicely) ---

print("\n--- Dividend Discount Model (DDM) Summary ---")
print(f"Cost of Equity (r): {cost_of_equity * 100:.2f}%")
print(f"Terminal Growth Rate (g): {terminal_growth * 100:.2f}%")

print("\nForecasted Dividends Per Share (DPS):", [f"${x:.2f}" for x in dps])
print("Years Away (for each dividend payment):", [f"{x:.2f}" for x in years_away])
print("Discounted Dividends:", [f"${x:.2f}" for x in discounted_dividends])

print(f"\nPresent Value of Dividends: ${present_value_dividends:.2f}")
print(f"Terminal Year DPS: ${terminal_dps:.2f}")
print(f"Terminal Value (undiscounted): ${terminal_value:.2f}")
print(f"Discounted Terminal Value: ${discounted_terminal_value:.2f}")

print(f"\nIntrinsic Value / Implied Share Price: ${intrinsic_value:.2f}")