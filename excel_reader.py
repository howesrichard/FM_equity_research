import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import requests as rq
import lxml
import fpdf
import yfinance as yf
import ipywidgets as ipy

# Read the excel file
df = pd.read_excel('example_files/DCF_test.xlsx', sheet_name="Sheet1", usecols='A:L', skiprows=0, nrows=4)

# We can check if Python and Excel achieve the same NPV value

excel_npv = df.iloc[-1,1] # get the NPV value from the last row and second column

python_npv = sum(df.iloc[0, 1:] * df.iloc[1, 1:]) # calculate the NPV using Python

print(f'Excel NPV: {excel_npv:,.2f}')
print(f'Python NPV: {python_npv:,.2f}')