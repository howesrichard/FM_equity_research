from fpdf import FPDF
from financial_ratios import Stock
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Assigning ticker symbol
TICKER = "HUB.AX"

# Fetching financial metric data
def get_financial_metrics(ticker:str):
    # Getting data using function from financial_ratios.py
    stock = Stock(ticker=TICKER)
    forward_pe = stock.get_forward_pe()
    debt_to_equity = stock.get_debt_to_equity()
    return_on_equity = stock.get_return_on_equity()
    operating_margin = stock.get_operating_margin()
    dividend_yield = stock.get_dividend_yield()
    return forward_pe, debt_to_equity, return_on_equity, operating_margin, dividend_yield

document = FPDF() #Creating a PDF object

def create_initial_pdf():
    document.add_page()
    document.set_margins(left=15, top=15, right=15)
    document.set_font(family='Arial', style='B', size=11) # Setting font to fully initialise object

    # Calculate the width of the title text
    title_text = 'Hub24 Equity Research Report'
    title_width = document.get_string_width(title_text)

    # Adding title by specifying formatting then position and text
    document.set_font(family='Arial', style='B', size=20)

    # Creating a filled rectangle at the top of the page to go with title
    document.set_fill_color(200, 200, 200)
    top_band_height = document.w * 0.1
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
    document.set_font(family='Arial', size=11)
    document.multi_cell(w=0, h=5, txt=company_overview_text, border=False, align='L', fill=False)

def add_financial_metrics_section(): # This function must be called after get_financial_metrics()
    #Creating a table for financial metrics
    document.set_font(family='Arial', style='', size=16)
    document.cell(w=0,
                  h=10,
                  txt='Figure 1: Key Financial Metrics',
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
    
    # Return the cursor position for the chart that can be called upon across functions
    metric_x = document.get_x()
    metric_y = document.get_y()
    return metric_x, metric_y

def add_Investment_Thesis():
    # Adding title
    document.set_xy(metric_x, metric_y + 5)
    document.set_font(family='Arial', style='', size=16)
    document.cell(w=0,
                  h=10,
                  txt='Investment Thesis',
                  border=False,
                  ln=1,
                  align='L',
                  fill=False)
    
    # Reading the investment thesis overview from a file
    with open('thesis_overview.txt', 'r') as file:
        thesis_pt1 = file.read()
    
    # Formatting the investment thesis overview 
    document.set_font(family='Arial', size=11)
    document.set_text_color(0, 0, 0)  # Reset text color to black
    document.multi_cell(w=70, 
                        h=5,
                        txt=thesis_pt1,
                        border=False,
                        align='L',
                        fill=False) 
    pt1_x = document.get_x()
    pt1_y = document.get_y()
    
    # Formatting the thesis elaboration
    sections = [
    ("Valuation Concerns", "thesis_valuation.txt"),
    ("Competitive Pressures", "thesis_comp.txt"),
    ("Insider Trading", "thesis_insider.txt")]

    for bold_text, commentary_file in sections:
        # Add bold text
        document.set_font(family='Arial', style='B', size=12)
        document.multi_cell(w=0, h=10, txt=bold_text, border=False, align='L', fill=False)
        # Read commentary from the file
        with open(commentary_file, 'r') as file:
            commentary = file.read()
        # Add commentary
        document.set_font(family='Arial', style='', size=11)
        document.multi_cell(w=0, h=5, txt=commentary, border=False, align='L', fill=False)

# Adds chart showing hub24 share price history / target price history and ASX share price history
def add_Chart():
    # Import necessary libraries
    import yfinance as yf

    # Step 1: Retrieve HUB24 and ASX200 historical price data from Yahoo Finance
    def fetch_price_data(ticker, start_date, end_date): # originally fetch_price_data
        historical_prices = yf.download(ticker, start=start_date, end=end_date) #originally stock_data
        return historical_prices['Close']

    # HUB24 (ASX: HUB) and ASX200 (^AXJO) tickers
    hub24_ticker = "HUB.AX"
    asx200_ticker = "^AXJO"

    # Define date range
    start_date = "2020-05-05"
    end_date = "2025-04-29"

    # Fetch data
    hub24_prices = fetch_price_data(hub24_ticker, start_date, end_date)
    asx200_prices = fetch_price_data(asx200_ticker, start_date, end_date)

    # Step 2: Load historical price targets from CSV
    price_targets = "price_targets.csv"  # Replace with your actual file path
    price_targets = pd.read_csv(price_targets, parse_dates=["Date"]) 
    price_targets.set_index("Date", inplace=True)
    
    # Step 3: Plot the data with two y-axes
    fig, ax1 = plt.subplots(figsize=(11, 6))

    # Plot ASX200 price history on the primary y-axis
    asx200_price = ax1.plot(asx200_prices, label="ASX200 Index", color="orange")
    ax1.set_xlabel("Date", fontsize=18)
    ax1.set_ylabel("ASX200 Price (AUD)", fontsize=20, color="orange")
    ax1.tick_params(axis='y', labelsize=15,labelcolor="orange")
    ax1.tick_params(axis='x', labelsize=15)
    ax1.grid()

    # Create a secondary y-axis for HUB24 prices
    ax2 = ax1.twinx()

    # Plot HUB24 Price history on secondary y-axis
    hub24_price = ax2.plot(hub24_prices, label="HUB24 Price History", color="blue")
    ax2.set_ylabel("HUB24 Price (AUD)", fontsize=20, color="blue")
    ax2.tick_params(axis='y', labelsize=15,labelcolor="blue")

    # Plot HUB24 price targets on secondary y-axis
    price_targets = ax2.plot(price_targets.index, price_targets['12M Tgt. Price'], label="HUB24 Price Targets", color="red", linestyle="--")

    # Add a title
    plt.title("HUB24 and ASX200 Price History", fontsize=25)
    fig.tight_layout()

    # Adding legend for three graphs
    custom_labels = ["ASX200 Price History", "HUB24 Price History", "HUB24 Price Targets"]
    lines = [asx200_price[0], hub24_price[0], price_targets[0]] # both variables are lists of lines due to plot() function's nature, hence [0] is used to retrieve the line object within the lists
    ax1.legend(lines, custom_labels, fontsize=15, loc="upper left")

    # Save and show the chart
    chart = "hub24_asx200_dual_axis_chart.png" #
    plt.savefig(chart) 
    plt.close()

    # Add the graph 70 mm right of financial metrics table
    graph_y_position = metric_y + 5 
    graph_x_position = metric_x + 70
    document.image("hub24_asx200_dual_axis_chart.png", x=graph_x_position, y=graph_y_position, w=110, h=60)

def add_Operating_Model():
    # Adding new page for financials and model
    document.add_page()
    document.set_font(family='Arial',
                  style='',
                  size=16)
    document.cell(w=0, h=10, txt='Figure 2: Operating Model', border=False, ln=1, align='L', fill=False)
    subtitle_text = 'Figure 2: Operating Model'
    # Operating Model
    table1 = pd.read_excel("HUB24 DCF Model.xlsx", usecols="B:J", skiprows=10, nrows=18).dropna()
    # Round numeric values to 2 decimal places
    table1 = table1.map(lambda x: round(x, 2) if isinstance(x, (int, float)) else x)
    
    cell_number = 1 # used for table header formatting
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

    # Formatting table to to ensure correct widths
    for i in range(1, len(table1)):
        for j in range(len(table1.columns)):
            text = table1.iloc[i, j]
            if j == 0:
                document.cell(w=35, h=10, txt=str(text), ln=0,align='L', fill=False, border=True)
            else:
                document.cell(w=18, h=10, txt=str(text), ln=0,align='C', fill=False, border=True)
    
        document.ln(10)
    
    # Adding commentary below the table
    with open('Valuation Commentary.txt', 'r') as file:
        valuation_commentary = file.read()

    document.ln(3)
    document.set_font(family='Arial', style='', size=11)
    document.multi_cell(w=0,
                        h=5,
                        txt=valuation_commentary,
                        border=False,
                        align='L',
                        fill=False)    

def add_Distilling_Share_Price():
    document.set_font(family='Arial',
                  style='',
                  size=16)
    document.cell(w=0, h=10, txt='Figure 3: Distilling Share Price', border=False, ln=1, align='L', fill=False)
    subtitle_text = 'Figure 3: Distilling Share Price'
    
    document.set_font(family='Arial', style='', size=9)
    table2 = pd.read_excel("HUB24 DCF Model.xlsx", usecols="B:C", skiprows=30, nrows=21).dropna()

    column_name = table2.columns[1]
    table2[column_name] = table2[column_name].astype(object)
    table2.iloc[1, 1] = f"{table2.iloc[1, 1] * 100:.2f}%"
    table2.iloc[-1, 1] = f"{table2.iloc[-1, 1] * 100:.2f}%"

    # Adding table headers
    document.set_fill_color(200,200,200)
    document.cell(w=60, h=6, txt=str(table2.columns[0]), ln=0, align='L', fill=True, border=True)
    document.cell(w=20, h=6, txt=f"{table2.columns[1]:.2f}", ln=1, align='L', fill=False, border=True)

    # Adding table data
    for index, row in table2.iterrows():
        document.cell(w=60,
                      h=6,
                      txt=str(row.iloc[0]),
                      ln=0, align='L',
                      fill=True,
                      border=True)
        document.cell(w=20,
                      h=6,
                      txt=f"{row.iloc[1]:.2f}" if isinstance(row.iloc[1], (int, float)) else str(row.iloc[1]),
                      ln=1,
                      align='L',
                      fill=False,
                      border=True)

def add_Sensitivity_Table():
    # Importing table from excel and formatting cells as needed
    table3 = pd.read_excel("HUB24 DCF Model.xlsx", usecols="E:J", skiprows=34, nrows=6).dropna()
    table3.columns = ['TGR', 5.5, 6.0, 6.5, 7.0, 7.5]
    table3['TGR'] = table3['TGR'] * 100
    table3['TGR'] = np.round(table3['TGR'],2)    
    table3.set_index('TGR', inplace=True)

    # Using Seaborn to create a heatmap for the sensitivity table
    sns.heatmap(data=table3, annot=True, cmap='RdYlGn', square=False, alpha = 0.8, cbar=False)
    plt.title(label='DCF Share Price Sensitivity', fontsize=16)
    plt.ylabel(ylabel='TGR(%)', fontsize=14)
    plt.xlabel(xlabel='WACC (%)', fontsize=14)
    
    # Saving the heatmap output
    plot_path = 'heatmap.png'
    plt.savefig(plot_path, dpi=200, bbox_inches='tight')
    plt.close()

    # Adding the heatmap to the PDF
    document.image(plot_path, x=100, y=183, w=95, h=86)
    document.set_xy(x=100, y=173)
    document.set_font(family='Arial', style='', size=16)
    document.cell(w=0, h=10, txt='Figure 4: Sensitivity Analysis', border=False, ln=1, align='L', fill=False)

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

# Calling functions to create the report
create_initial_pdf()
add_logo()
add_company_overview()
forward_pe, debt_to_equity, return_on_equity, operating_margin, dividend_yield = get_financial_metrics(TICKER)
metric_x, metric_y = add_financial_metrics_section() # Call the function to get the x and y positions
add_Investment_Thesis()
add_Chart()
add_Operating_Model()
add_Distilling_Share_Price()
add_Sensitivity_Table()

# Saving contents to PDF file
document.output(name='Group_45_HUB24_Report.pdf')