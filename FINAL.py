# Import libraries

import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt
import requests as rq 
import lxml 
import fpdf 
import yfinance as yf 
import ipywidgets as ipy 

# Basic functions

# Function to calculate the P/E ratio of a stock
def calculate_pe_ratio(price, earnings):
    return price / earnings

# Function to calculate the dividend yield of a stock
def calculate_dividend_yield(dividend, price):
    return dividend / price
    
# Function to calculate the earnings per share of a stock
def calculate_eps(net_income, shares_outstanding):
    return net_income / shares_outstanding
    
# Function to calculate ROA of a stock
def calculate_roa(net_income, total_assets):
    return net_income / total_assets


# Pick company

ticker = input("Enter the ticker of the company you want to analyse: ")
company = yf.Ticker(ticker)
company_info = company.info
company_info

# Financials
financials = company.financials
financials

# Balance Sheet
balance_sheet = company.balance_sheet
balance_sheet

#Cash Flow
cash_flow = company.cashflow
cash_flow

# Earnings
earnings = company.earnings
earnings

# Sustainability
sustainability = company.sustainability
sustainability

# Options

options = company.options
options

# Dividends

dividends = company.dividends
dividends

# Actions

actions = company.actions
actions

# Major Holders

major_holders = company.major_holders
major_holders

# Institutional Holders

institutional_holders = company.institutional_holders
institutional_holders

# Analysis

analysis = company.recommendations
analysis

# Calendar

calendar = company.calendar
calendar 

# History

history = company.history(period="max")
history

# Create a PDF
pdf = fpdf.FPDF(format='letter')
pdf.add_page()
pdf.set_font("Arial", size=12)

# Title
pdf.cell(200, 20, txt="EQUITY REPORT", ln=True, align="C")

# Key Ratios Section
pdf.cell(200, 10, txt="Key Ratios", ln=True, align="C")

try:
    # P/E Ratio
    pe_ratio = calculate_pe_ratio(earnings.get("Net Income", 0), earnings.get("Shares Outstanding", 0))
    pdf.cell(200, 10, txt=f"P/E Ratio: {pe_ratio}", ln=True, align="L")
except Exception as e:
    pdf.cell(200, 10, txt=f"P/E Ratio: Error ({e})", ln=True, align="L")

try:
    # Dividend Yield
    dividend_yield = calculate_dividend_yield(dividends.get("Dividends", 0), history["Close"].iloc[-1])
    pdf.cell(200, 10, txt=f"Dividend Yield: {dividend_yield}", ln=True, align="L")
except Exception as e:
    pdf.cell(200, 10, txt=f"Dividend Yield: Error ({e})", ln=True, align="L")

try:
    # Earnings per Share
    eps = calculate_eps(earnings.get("Net Income", 0), earnings.get("Shares Outstanding", 0))
    pdf.cell(200, 10, txt=f"Earnings per Share: {eps}", ln=True, align="L")
except Exception as e:
    pdf.cell(200, 10, txt=f"Earnings per Share: Error ({e})", ln=True, align="L")

try:
    # Return on Assets
    roa = calculate_roa(earnings.get("Net Income", 0), balance_sheet.get("Total Assets", 0))
    pdf.cell(200, 10, txt=f"Return on Assets: {roa}", ln=True, align="L")
except Exception as e:
    pdf.cell(200, 10, txt=f"Return on Assets: Error ({e})", ln=True, align="L")

# Financial Metrics Section
pdf.cell(200, 10, txt="Financial Metrics", ln=True, align="C")

try:
    # Net Income
    net_income = earnings.get("Net Income", "N/A")
    pdf.cell(200, 10, txt=f"Net Income: {net_income}", ln=True, align="L")
except Exception as e:
    pdf.cell(200, 10, txt=f"Net Income: Error ({e})", ln=True, align="L")

try:
    # Total Assets
    total_assets = balance_sheet.get("Total Assets", "N/A")
    pdf.cell(200, 10, txt=f"Total Assets: {total_assets}", ln=True, align="L")
except Exception as e:
    pdf.cell(200, 10, txt=f"Total Assets: Error ({e})", ln=True, align="L")

try:
    # Shares Outstanding
    shares_outstanding = earnings.get("Shares Outstanding", "N/A")
    pdf.cell(200, 10, txt=f"Shares Outstanding: {shares_outstanding}", ln=True, align="L")
except Exception as e:
    pdf.cell(200, 10, txt=f"Shares Outstanding: Error ({e})", ln=True, align="L")

try:
    # Dividends
    dividends_value = dividends.get("Dividends", "N/A")
    pdf.cell(200, 10, txt=f"Dividends: {dividends_value}", ln=True, align="L")
except Exception as e:
    pdf.cell(200, 10, txt=f"Dividends: Error ({e})", ln=True, align="L")

try:
    # Close Price
    close_price = history["Close"].iloc[-1]
    pdf.cell(200, 10, txt=f"Close Price: {close_price}", ln=True, align="L")
except Exception as e:
    pdf.cell(200, 10, txt=f"Close Price: Error ({e})", ln=True, align="L")

# Save the PDF
try:
    pdf.output("Company Analysis.pdf")
    print("PDF successfully created: Company Analysis.pdf")
except Exception as e:
    print(f"Error saving PDF: {e}")

# Plot the historical stock prices

plt.figure(figsize=(10, 6))
plt.plot(history.index, history["Close"], label=ticker)
plt.title(f"{ticker} Stock Price")
plt.xlabel("Date")
plt.ylabel("Price")
plt.legend()
plt.grid(True)
plt.show()
