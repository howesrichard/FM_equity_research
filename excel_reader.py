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

excel_npv = df.iloc[-1,1] 

def npv(row, column):
    return excel_npv

print(npv(-1,1))

