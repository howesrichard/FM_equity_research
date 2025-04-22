from fpdf import FPDF
from financial_ratios import get_financial_metrics

# Assigning ticker symbol
TICKER = "HUB.AX"

# Fetching financial metric data
financial_metrics = get_financial_metrics(TICKER)

# Creating PDF document
document = FPDF()
document.add_page()
document.set_margins(left=20, top=20, right=20)

# Adding title by specifying formatting then position and text
document.set_font(family='Arial', style='B', size=16)

# Calculate the width of the title text
title_text = 'Hub24 Equity Research Report'
title_width = document.get_string_width(title_text)

# Get the page width and calculate the x position to center the title
page_width = document.w
x_position = (page_width - title_width) / 2

# Adding title by specifying formatting then position and text
document.set_font(family='Arial',
                  style='BU',
                  size=16)

document.set_xy(x_position, 20)
document.cell(w=title_width,
              h=10,
              txt=title_text,
              border=False,
              ln=1,
              align='C',
              fill=False)

document.set_font(family='Arial',
                  size=11)

document.multi_cell(w=0,
                    h=10,
                    txt='This report provides an overview of the financial performance of Hub24.',
                    border=False,
                    align='L',
                    fill=False)

# Saving contents to PDF file
document.output(name='sample_report.pdf')