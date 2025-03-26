# Import libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import requests as rq
import lxml
import fpdf
import yfinance as yf
import ipywidgets as ipy

# Fetch data from yfinance
ticker = input("Enter the ticker symbol (e.g., AAPL): ").upper()
company = yf.Ticker(ticker)

# Extract financial data
try:
    balance_sheet = company.balance_sheet
    financials = company.financials

    # Calculate key ratios
    current_assets = balance_sheet.loc["Total Current Assets"].iloc[1] if "Total Current Assets" in balance_sheet.index else 0
    current_liabilities = balance_sheet.loc["Total Current Liabilities"].iloc[1] if "Total Current Liabilities" in balance_sheet.index else 0
    total_debt = balance_sheet.loc["Total Liab"].iloc[1] if "Total Liab" in balance_sheet.index else 0
    total_equity = balance_sheet.loc["Total Stockholder Equity"].iloc[1] if "Total Stockholder Equity" in balance_sheet.index else 0
    revenue = financials.loc["Total Revenue"].iloc[1] if "Total Revenue" in financials.index else 0
    gross_profit = financials.loc["Gross Profit"].iloc[1] if "Gross Profit" in financials.index else 0
    net_income = financials.loc["Net Income"].iloc[1] if "Net Income" in financials.index else 0

    current_ratio = current_assets / current_liabilities if current_liabilities else 0
    quick_ratio = (current_assets - balance_sheet.loc["Inventory"].iloc[0]) / current_liabilities if "Inventory" in balance_sheet.index and current_liabilities else 0
    debt_to_equity = total_debt / total_equity if total_equity else 0
    gross_margin = (gross_profit / revenue) * 100 if revenue else 0
    net_margin = (net_income / revenue) * 100 if revenue else 0
    roa = (net_income / balance_sheet.loc["Total Assets"].iloc[1]) * 100 if "Total Assets" in balance_sheet.index else 0
    roe = (net_income / total_equity) * 100 if total_equity else 0
    roi = roa  # Assuming ROI is the same as ROA for simplicity
except Exception as e:
    print(f"Error fetching financial data: {e}")
    current_ratio = quick_ratio = debt_to_equity = gross_margin = net_margin = roa = roe = roi = 0

# Make a PDF
pdf = fpdf.FPDF()
pdf.add_page()

# Add a title
pdf.set_font("Arial", size=12)
pdf.cell(200, 10, "Financial Analysis of a Company", 0, 1, "C")

# Add a subtitle
pdf.set_font("Arial", size=9)
pdf.cell(200, 10, "Key Ratios", 0, 1, "C")

# Add a table for Key Ratios
pdf.set_font("Arial", size=9)
pdf.cell(60, 10, "Current Ratio", 1, 0, "C")
pdf.cell(60, 10, "Quick Ratio", 1, 0, "C")
pdf.cell(60, 10, "Debt to Equity", 1, 1, "C")

# Add data for Key Ratios
pdf.cell(60, 10, f"{current_ratio:.2f}", 1, 0, "C")
pdf.cell(60, 10, f"{quick_ratio:.2f}", 1, 0, "C")
pdf.cell(60, 10, f"{debt_to_equity:.2f}", 1, 1, "C")

# Add a subtitle
pdf.cell(200, 10, "Key Metrics", 0, 1, "C")

# Add a table for Key Metrics
pdf.cell(60, 10, "Revenue", 1, 0, "C")
pdf.cell(60, 10, "Gross Margin", 1, 0, "C")
pdf.cell(60, 10, "Net Margin", 1, 1, "C")

# Add data for Key Metrics
pdf.cell(60, 10, f"{revenue/1e6:.2f}M", 1, 0, "C")
pdf.cell(60, 10, f"{gross_margin:.2f}%", 1, 0, "C")
pdf.cell(60, 10, f"{net_margin:.2f}%", 1, 1, "C")

# Add a subtitle
pdf.cell(200, 10, "Profitability Metrics", 0, 1, "C")

# Add a table for Profitability Metrics
pdf.cell(60, 10, "ROA", 1, 0, "C")
pdf.cell(60, 10, "ROE", 1, 0, "C")
pdf.cell(60, 10, "ROI", 1, 1, "C")

# Add data for Profitability Metrics
pdf.cell(60, 10, f"{roa:.2f}%", 1, 0, "C")
pdf.cell(60, 10, f"{roe:.2f}%", 1, 0, "C")
pdf.cell(60, 10, f"{roi:.2f}%", 1, 1, "C")

# Save the PDF
pdf.output("Financial Analysis.pdf")
print("✅ Financial Analysis PDF generated successfully!")