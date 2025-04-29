import pandas as pd
import os
import matplotlib.pyplot as plt

# retrieve excel file and load
current_dir = os.path.dirname(__file__)
file_path = os.path.join(current_dir, 'BENDIGO.xlsx')
df = pd.read_excel(file_path, sheet_name='Dividend Discount Model', header=None)

# pull cost of equity from J11
cost_of_equity = float(df.iloc[11, 9])

# pull terminal growth rate from J13
terminal_growth = float(df.iloc[12, 9])

# convert to decimal
cost_of_equity = cost_of_equity / 100 if cost_of_equity > 1 else cost_of_equity
terminal_growth = terminal_growth / 100 if terminal_growth > 1 else terminal_growth

# dividends per share
dps = df.iloc[30, 13:18].astype(float).values

# years away
years_away = df.iloc[33, 13:18].astype(float).values

# terminal year DPS
terminal_dps = float(df.iloc[41, 9])

# terminal years away
terminal_years_away = float(df.iloc[45, 9])

# DDM Calculations

# discounted dividends
discounted_dividends = dps / (1 + cost_of_equity) ** years_away
present_value_dividends = discounted_dividends.sum()

# terminal value
terminal_value = (terminal_dps * (1 + terminal_growth)) / (cost_of_equity - terminal_growth)

# discounted terminal value
discounted_terminal_value = terminal_value / (1 + cost_of_equity) ** terminal_years_away

# total intrinsic value
intrinsic_value = present_value_dividends + discounted_terminal_value

# print summary

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

# create DDM table

# read the specific range of data (D25 to R35)
data=df = pd.read_excel(file_path, sheet_name='Dividend Discount Model', usecols='D:R', skiprows=24, nrows=11)

# remove columns F to J
data.drop(data.columns[2:7], axis=1, inplace=True)

# remove row 8
data.drop([7], axis=0, inplace=True)

# replace NaN values (empty cells) with blank cells 
data.fillna('', inplace=True)

# round all numeric values to 2 decimal places
data = data.applymap(lambda x: round(x, 2) if isinstance(x, (int, float)) else x)

# create a period row with years
periods = ['Period'] + [''] + ['FY2022', 'FY2023', 'FY2024', 'FY2025', 'FY2026', 'FY2027', 'FY2028', 'FY2029']
periods_df = pd.DataFrame([periods], columns=data.columns)
data = pd.concat([periods_df, data], ignore_index=True)

# plot the table
fig, ax = plt.subplots(figsize=(12,6))  # Create a figure and axis

# display the data as a table
table = ax.table(cellText=data.values, colLabels=data.columns, cellLoc='center', loc='center')

# customise table appearance
table.auto_set_font_size(False) 
table.set_fontsize(10)
table.scale(1, 1.5)  

# far left column is slightly longer, and thus needs to be increased
table.auto_set_column_width([0])

# remove axis
ax.axis('off')

# change colours of the cells to match the excel and bold important lines

for col in range(2, 10):
    table[(2, col)].set_text_props(color='royalblue')

for col in range(2, 10):
    table[(3, col)].set_text_props(color='darkgreen')

for col in range(2, 5):
    table[(7, col)].set_text_props(color='royalblue')

for col in range(len(data.columns)):
    table[(10, col)].set_text_props(weight='bold')

for col in range(len(data.columns)):
    table[(1, col)].set_text_props(weight='bold')

# remove the gridlines for the table
for (i, j), cell in table.get_celld().items():
    cell.set_edgecolor('white') 
    cell.set_linewidth(0)  

# highlight row 2 in light gray
for col in range(len(data.columns)):
    cell = table[(1, col)]
    cell.set_facecolor('#f0f0f0') 

# show the plot with the table
plt.show()

