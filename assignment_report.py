from fpdf import FPDF
from financial_ratios import Stock

# Assigning ticker symbol
TICKER = "HUB.AX"

# Fetching financial metric data
HUB = Stock(ticker=TICKER)
forward_pe = HUB.get_forward_pe()
debt_to_equity = HUB.get_debt_to_equity()
return_on_equity = HUB.get_return_on_equity()
operating_margin = HUB.get_operating_margin()
dividend_yield = HUB.get_dividend_yield()

# Creating PDF document
document = FPDF()
document.add_page()
document.set_margins(left=15, top=15, right=15)

# Adding title by specifying formatting then position and text
document.set_font(family='Arial', style='B', size=16)

# Calculate the width of the title text
title_text = 'Hub24 Equity Research Report'
title_width = document.get_string_width(title_text)

# Get the page width and calculate the x position to center the title
page_width = document.w
x_position = (page_width - title_width) / 2

# Adding title by specifying formatting then position and text
document.set_font(family='Arial', style='BU', size=16)

document.set_xy(x_position, 20)
document.cell(w=title_width,
              h=10,
              txt=title_text,
              border=False,
              ln=1,
              align='C',
              fill=False)

document.set_font(family='Arial', size=11)

document.multi_cell(w=0,
                    h=10,
                    txt='This report provides an overview of the financial performance of Hub24.',
                    border=False,
                    align='L',
                    fill=False)

#Creating a table for financial metrics
document.set_font(family='Arial', style='B', size=12)

document.cell(w=0,
              h=10,
              txt='Financial Metrics',
              border=False,
              ln=1,
              align='C',
              fill=False)
document.set_font(family='Arial', size=11)
# Adding table headers
document.cell(w=60,
              h=10,
              txt='Metric',
              border=True,
              ln=0,
              align='C',
              fill=False)
document.cell(w=60,
              h=10,
              txt='Value',
              border=True,
              ln=1,
              align='C',
              fill=False)
# Adding table data
metrics = {
    "Forward P/E": forward_pe,
    "Debt to Equity": debt_to_equity,
    "Return on Equity": return_on_equity,
    "Operating Margin": operating_margin,
    "Dividend Yield": dividend_yield
}
for metric, value in metrics.items():
    document.cell(w=60,
                  h=10,
                  txt=metric,
                  border=True,
                  ln=0,
                  align='C',
                  fill=False)
    document.cell(w=60,
                  h=10,
                  txt=str(value),
                  border=True,
                  ln=1,
                  align='C',
                  fill=False)

# Saving contents to PDF file
document.output(name='sample_report.pdf')