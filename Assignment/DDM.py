import pandas as pd
import os
import matplotlib.pyplot as plt

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

# Read the specific range of data (D25 to R35)
data=df = pd.read_excel(file_path, sheet_name='Dividend Discount Model', usecols='D:R', skiprows=24, nrows=11)


# Drop columns F to J (indices 2 to 6)
data.drop(data.columns[2:7], axis=1, inplace=True)

# Drop row 8 (index 7)
data.drop([7], axis=0, inplace=True)

# Replace NaN values with blank cells (empty string)
data.fillna('', inplace=True)

# Round all numeric values to 2 decimal places
data = data.applymap(lambda x: round(x, 2) if isinstance(x, (int, float)) else x)

# Create a list for the top row (dates/periods)
periods = ['Period'] + [''] + ['FY2022', 'FY2023', 'FY2024', 'FY2025', 'FY2026', 'FY2027', 'FY2028', 'FY2029']

# Convert the list into a DataFrame for concatenation
periods_df = pd.DataFrame([periods], columns=data.columns)

# Prepend the new row to the existing data
data = pd.concat([periods_df, data], ignore_index=True)

# Create the plot and table
fig, ax = plt.subplots(figsize=(12,6))  # Create a figure and axis

# Hide the axes to display only the table
ax.axis('off')

# Display the data as a table
table = ax.table(cellText=data.values, colLabels=data.columns, cellLoc='center', loc='center')

# Customize table appearance (optional)
table.auto_set_font_size(False) 
table.set_fontsize(10)
table.scale(1, 1.5)  # Adjust table size

# Adjust the far-left column width
table.auto_set_column_width([0])  # Set the width of the first column

# Set the color for specific cells
# Row 1, columns 2-9: Royal blue
for col in range(2, 10):
    table[(2, col)].set_text_props(color='royalblue')

# Row 2, columns 2-9: Dark green
for col in range(2, 10):
    table[(3, col)].set_text_props(color='darkgreen')

# Row 6, columns 2-4: Royal blue
for col in range(2, 5):
    table[(7, col)].set_text_props(color='royalblue')

# Bold row 9 (index 8)
for col in range(len(data.columns)):
    table[(10, col)].set_text_props(weight='bold')

# Show the plot with the table
plt.show()

