import pandas as pd
import numpy as np

def read_dcf_summary(filepath):
    """
    Reads key DCF output from Excel file and returns a summary dictionary.
    """
    try:
        df = pd.read_excel(filepath, sheet_name=0)
        summary = {
            "DCF Valuation": float(df.iloc[0, 1]),
            "WACC": float(df.iloc[1, 1]),
            "Terminal Growth Rate": float(df.iloc[2, 1]) if not pd.isna(df.iloc[2, 1]) else None,
            "Implied Share Price": float(df.iloc[3, 1])
        }
        return summary
    except Exception as e:
        return f"Error reading DCF: {e}"

# 👉 Run the function using the correct file path:
result = read_dcf_summary("example_files/DCF_test.xlsx")
print("DCF OUTPUT:\n")
print(result)
