from fpdf import FPDF
from financial_functions import calculate_pe_ratio, calculate_roe, calculate_ebitda_margin
from read_dcf import read_dcf_summary
from read_commentary import read_commentary

# Data Inputs
pe = calculate_pe_ratio(14.50, 1.32)
roe = calculate_roe(250_000_000, 2_100_000_000)
ebitda_margin = calculate_ebitda_margin(720_000_000, 2_800_000_000)
dcf = read_dcf_summary("example_files/DCF_test.xlsx")
commentary = read_commentary("example_files/commentary.txt")

# PDF Setup
pdf = FPDF()
pdf.add_page()
pdf.set_font("Arial", size=12)

# Title
pdf.set_font("Arial", 'B', 16)
pdf.cell(0, 10, "Equity Research Report", ln=True, align="C")
pdf.ln(10)

# Ratios
pdf.set_font("Arial", 'B', 12)
pdf.cell(0, 10, "Key Financial Ratios:", ln=True)
pdf.set_font("Arial", size=12)
pdf.cell(0, 10, f"P/E Ratio: {pe}", ln=True)
pdf.cell(0, 10, f"ROE: {roe}", ln=True)
pdf.cell(0, 10, f"EBITDA Margin: {ebitda_margin}", ln=True)
pdf.ln(5)

# DCF Summary
pdf.set_font("Arial", 'B', 12)
pdf.cell(0, 10, "DCF Valuation Summary:", ln=True)
pdf.set_font("Arial", size=12)
for key, value in dcf.items():
    pdf.cell(0, 10, f"{key}: {value}", ln=True)
pdf.ln(5)

# Commentary
pdf.set_font("Arial", 'B', 12)
pdf.cell(0, 10, "Analyst Commentary:", ln=True)
pdf.set_font("Arial", size=12)
pdf.multi_cell(0, 10, commentary)

# Output
pdf.output("equity_research_report.pdf")
print("PDF report generated: equity_research_report.pdf ✅")