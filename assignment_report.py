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

def add_company_overview():
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
                  size=11)
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

def add_Operating_Model():
    import pandas as pd
    document.add_page()
    document.set_font(family='Arial',
                  style='',
                  size=16)
    document.cell(w=0, h=10, txt='Figure 2: Operating Model', border=False, ln=1, align='L', fill=False)
    subtitle_text = 'Figure 2: Operating Model'
    # Operating Model
    table1 = pd.read_excel("HUB24 DCF Model.xlsx", usecols="B:J", skiprows=10, nrows=18).dropna()
    # Round numeric values to 2 decimal places
    table1 = table1.applymap(lambda x: round(x, 2) if isinstance(x, (int, float)) else x)

    cell_number = 1
    for column_name in table1.columns.astype(str):
        document.set_fill_color(0, 0, 100)  # Set fill colour to dark blue
        document.set_text_color(255, 255, 255) # Set text colour to white
        document.set_font(family='Arial', style='B', size=11)
        if cell_number == 1:
            document.cell(w=35, h=10, txt=str(column_name), ln=0,align='L', fill=True, border=True)
            cell_number += 1
        else:
            document.cell(w=18, h=10, txt=str(column_name), ln=0,align='C', fill=True, border=True)
    document.ln(10)

    document.set_text_color(0, 0, 0)  # Reset text colour to black
    document.set_font(family='Arial', style='', size=9)

    for i in range(1, len(table1)):
        for j in range(len(table1.columns)):
            text = table1.iloc[i, j]
            if j == 0:
                document.cell(w=35, h=10, txt=str(text), ln=0,align='L', fill=False, border=True)
            else:
                document.cell(w=18, h=10, txt=str(text), ln=0,align='C', fill=False, border=True)
        document.ln(10)

def add_logo():
    import requests
    import cairosvg
    from PIL import Image
    from io import BytesIO

    # URL of the image
    image_url = "https://www.hub24.com.au/wp-content/uploads/2021/10/hub24-logo-light.svg"

    # Send GET request to URL
    response = requests.get(image_url)

    # Check if request was successful
    if response.status_code == 200:
        # Convert SVG to PNG
        png_data = cairosvg.svg2png(bytestring=response.content)
        image = Image.open(BytesIO(png_data))

        # Create a new image with a grey background
        grey_background = Image.new("RGB", image.size, (200, 200, 200))
        image = image.convert("RGBA")
        grey_background.paste(image, mask=image.split()[3]) 

        # Save the image as a JPEG
        grey_background.save("downloaded_image.jpg", "JPEG")

        # Add image to PDF
        document.image("downloaded_image.jpg", x=15, y=10, w=30)  # Adjust x, y, and w as needed
    else:
        print(f"Failed to retrieve image. Status code: {response.status_code}")

create_initial_pdf()
add_logo()
add_company_overview()
forward_pe, debt_to_equity, return_on_equity, operating_margin, dividend_yield = get_financial_metrics(TICKER)
add_financial_metrics_section()
add_Operating_Model()

# Saving contents to PDF file
document.output(name='sample_report.pdf')

