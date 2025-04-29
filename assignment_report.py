from fpdf import FPDF
from financial_ratios import Stock

# Assigning ticker symbol
TICKER = "HUB.AX"

# Fetching financial metric data
def get_financial_metrics(ticker:str):
    stock = Stock(ticker=TICKER)
    forward_pe = stock.get_forward_pe()
    debt_to_equity = stock.get_debt_to_equity()
    return_on_equity = stock.get_return_on_equity()
    operating_margin = stock.get_operating_margin()
    dividend_yield = stock.get_dividend_yield()
    return forward_pe, debt_to_equity, return_on_equity, operating_margin, dividend_yield

document = FPDF()

def create_initial_pdf():
    document.add_page()
    document.set_margins(left=15, top=15, right=15)

    # Need to set font to initialise the object completely
    document.set_font(family='Arial', style='B', size=11)

    # Calculate the width of the title text
    title_text = 'Hub24 Equity Research Report'
    title_width = document.get_string_width(title_text)

    # Adding title by specifying formatting then position and text
    document.set_font(family='Arial', style='B', size=20)

    # Set fill color to grey for the title background
    document.set_fill_color(200, 200, 200)

    # Calculate the height for the top tenth of the page
    top_band_height = document.w * 0.1

    # Draw a filled rectangle for the title background
    document.rect(x=0, y=0, w=document.w, h=top_band_height, style='F')

    # Position the title text within the filled rectangle
    document.set_xy((document.w - title_width)/2, top_band_height / 2)
    document.cell(w=title_width,
                  h=10,
                  txt=title_text,
                  border=False,
                  ln=1,
                  align='C',
                  fill=False)

def add_commentary():
    # adding subtitle
    document.set_font(family='Arial',
                  style='',
                  size=16)
    document.cell(w=0, h=10, txt='Company Overview', border=False, ln=1, align='L', fill=False)
    subtitle_text = 'Company Overview'
    # Add commentary on the company overview
    with open("Company Overview.txt", "r") as file:
        company_overview_text = file.read()
    document.set_font(family='Arial',
                  size=10)
    document.multi_cell(w=0, h=5, txt=company_overview_text, border=False, align='L', fill=False)

def add_financial_metrics_section():
    #Creating a table for financial metrics
    document.set_font(family='Arial', style='', size=16)
    document.cell(w=0,
                  h=10,
                  txt='Key Financial Metrics',
                  border=False,
                  ln=1,
                  align='L',
                  fill=False)

    # Adding table headers
    document.set_font(family='Arial', size=12, style='B')
    document.set_text_color(255, 255, 255)  # Set text color to white
    document.set_fill_color(0, 0, 100)  # Set fill color to dark blue
    document.cell(w=50,
                  h=10,
                  txt='Metric',
                  border=True,
                  ln=0,
                  align='C',
                  fill=True)  # Enable fill
    document.cell(w=30,
                  h=10,
                  txt='Value',
                  border=True,
                  ln=0,
                  align='C',
                  fill=True)

    # Save current x and y positions
    x_start = document.get_x()
    y_start = document.get_y()

    # Add commentary to the right of the table
    with open('financial_metrics_commentary.txt', 'r') as file:
        commentary = file.read()

    document.set_xy(x_start + 5, y_start)
    document.set_font(family='Arial', size=11)
    document.set_text_color(0, 0, 0)  # Reset text color to black
    document.multi_cell(w=95,  # Width to fit the page symmetrically
                        h=5,
                        txt=commentary,
                        border=False,
                        align='L',
                        fill=False)

    # Reset position back to the start of the table
    document.set_xy(x_start - 80, y_start + 10)  # Move down for the table data

    # Adding table data
    metrics = {
        "Forward P/E": forward_pe,
        "Debt to Equity (%)": debt_to_equity,
        "Return on Equity (%)": return_on_equity,
        "Operating Margin(%)": operating_margin,
        "Dividend Yield(%)": dividend_yield
    }
    document.set_font(family='Arial', size=11)
    document.set_text_color(0, 0, 0)  # Reset text color to black
    for metric, value in metrics.items():
        document.cell(w=50,
                      h=10,
                      txt=metric,
                      border=True,
                      ln=0,
                      align='C',
                      fill=False)
        document.cell(w=30,
                      h=10,
                      txt=f"{value:.2f}" if isinstance(value, (int, float)) else str(value),
                      border=True,
                      ln=1,
                      align='C',
                      fill=False)

create_initial_pdf()
add_commentary()
forward_pe, debt_to_equity, return_on_equity, operating_margin, dividend_yield = get_financial_metrics(TICKER)
add_financial_metrics_section()

# Saving contents to PDF file
document.output(name='sample_report.pdf')