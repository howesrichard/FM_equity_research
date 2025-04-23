# Import from the FPDF libary
from fpdf import FPDF
# Demonstrate cursor movement

pdf = FPDF()
pdf.add_page()

# add a left border filled
pdf.set_fill_color(50,60,65)
#add grey/green left border
pdf.rect(x=0, y=0, w=5, h=297, style='F')
#add yellow next to grey left border
pdf.set_fill_color(253,243,83)
pdf.rect(x=5, y=0, w=2, h=297, style='F') 

# Left side of page (group names, date, ticker, and logo)

#insert logo
pdf.image('Vicinity Centres_logo.png', x=10, y=0, w=40, h=25) #adjust width and height as required
pdf.ln(15) #line break

#insert text below logo
#set font for the date
pdf.set_font("Arial", "", 10)
pdf.set_xy(10,20) # set cursor position for date (10 units from the left, 10 units from the 10)
pdf.cell(0, 10, "Date: 23 April, 2025", ln=True)

#set font for initiation coverage
pdf.set_font("Arial", "B", 12)
pdf.cell(0,10, 'Initiation of Coverage', align='L') #Initiation of coverage title on the left
pdf.ln(7) #line break

#text for investment recommendation
pdf.set_font('Arial', 'B', 12)
pdf.set_text_color(255,204,0) #set text colour to yellow
pdf.cell(0,10, 'HOLD', align='L')

#insert separation line
pdf.set_draw_color(0,0,0)
pdf.line(11, 45, 65, 45) #insert a line 
pdf.ln(7) # line break

#set font for pricing
pdf.set_font('Arial','', 10)
pdf.set_text_color(0,0,0)
pdf.cell(0,10,'Target Price (average): $2.36', align='L')
pdf.ln(7) #line break
pdf.cell(0,10, 'Current Price $2.26', align='L')
pdf.ln(7) #line break
pdf.cell(0,10, 'Upside: 2.65%', align='L')

#insert separation line
pdf.set_draw_color(0,0,0)
pdf.line(11, 67, 65, 67) #insert a line 
pdf.ln(7) # line break

# inserting team names
pdf.set_font('Arial', 'B', 10)
pdf.set_text_color(0,0,0)
pdf.cell(0,10, 'Authored by FINM3422 Team 34', align='L')
pdf.ln(5) #line break

# Ellie Manton
pdf.set_font('Arial','', 8)
pdf.cell(0,10, 'Ellie Manton', align='L')
pdf.ln(3) #line break
pdf.set_font('Arial','',8)
pdf.set_text_color(0,0,0)
pdf.cell(0,10,'48853712', align='L')
pdf.ln(3) # line break
pdf.set_text_color(0,0,0)
pdf.cell(0,10,'e.manton@student.uq.edu.au', align='L')
pdf.ln(5) #line break

# Senuthi Herath
pdf.set_font('Arial','', 8)
pdf.cell(0,10, 'Senuthi Herath', align='L')
pdf.ln(3) #line break
pdf.set_font('Arial','',8)
pdf.set_text_color(0,0,0)
pdf.cell(0,10,'XXX', align='L')
pdf.ln(3) # line break
pdf.set_text_color(0,0,0)
pdf.cell(0,10,'s.herathmudiyanselage@student.uq.edu.au', align='L')
pdf.ln(5) #line break

# James Mcoombes
pdf.set_font('Arial', '', 8)
pdf.cell(0,10, 'James Mcoombes', align='L')
pdf.ln(3) #line break
pdf.set_font('Arial','',8)
pdf.set_text_color(0,0,0)
pdf.cell(0,10,'XXX', align='L')
pdf.ln(3) # line break
pdf.set_text_color(0,0,0)
pdf.cell(0,10,'j.mccoombes@student.uq.edu.au', align='L')
pdf.ln(5) #line break

# Sam Coronis
pdf.set_font('Arial', '', 8)
pdf.cell(0,10, 'Sam Coronis', align='L')
pdf.ln(3) #line break
pdf.set_font('Arial','',8)
pdf.set_text_color(0,0,0)
pdf.cell(0,10,'XXX', align='L')
pdf.ln(3) # line break
pdf.set_text_color(0,0,0)
pdf.cell(0,10,'s.coronis@student.uq.edu.au', align='L')
pdf.ln(5) #line break

#Right side of the page (header, intro, company overview, and company highlights)
# set font for the header
pdf.set_font("Arial", "B", 16)
pdf.set_text_color(0,0,0)
pdf.set_xy(72, 8)
pdf.cell(0, 10, "Equity Research Report: Vicinity Centres")
pdf.ln(10) #line break

#Paragraph 1 - Introduction

#Setting font for introductory title
pdf.set_font("Arial", "B", 10)
pdf.set_xy(72,19)
pdf.cell(0,10, 'Vicinity Centres (ASX: VCX)')

#insert separation line
pdf.set_draw_color(0,0,0)
pdf.line(73, 27, 200, 27) #insert a line 

#introduction body text
#import text from file
with open('Introduction.txt', 'r') as file:
    introduction_text = file.read()
#Replace unsupported characters for FPDF
introduction_text = introduction_text.replace("’", "'").replace("“", '"').replace("”", '"').replace("–", "-").replace("—", "-")
# set font for introduction text
pdf.set_font('Arial','',10)
pdf.set_text_color(0,0,0)
pdf.set_xy(72,29)
pdf.multi_cell(129,3.5, introduction_text, align='J')

#Paragraph 2 - Company Overview

#setting font for company overview title
pdf.set_font("Arial", "B", 10)
pdf.set_text_color(0,0,0)
pdf.set_xy(72,70)
pdf.cell(100,10, 'Company Overview')

#insert separation line
pdf.set_draw_color(0,0,0)
pdf.line(73, 78, 200, 78) #insert a line 

#Pull company overview text
#import text from file
with open('Company Overview.txt', 'r') as file:
    company_overview_text = file.read()
#Replace unsupported characters for FPDF
company_overview_text = company_overview_text.replace("’", "'").replace("“", '"').replace("”", '"').replace("–", "-").replace("—", "-")
#Set font for company overview text
pdf.set_font('Arial','',10)
pdf.set_text_color(0,0,0)
pdf.set_xy(72,80)
pdf.multi_cell(129,4, company_overview_text, align='J')

#Paragraph 3 - Company Highlights
#setting font for company highlights title
pdf.set_font("Arial", "B", 10)
pdf.set_text_color(0,0,0)
pdf.set_xy(72,143)
pdf.cell(100,10, 'Company Highlights')
pdf.ln(10) #line break

#insert separation line
pdf.set_draw_color(0,0,0)
pdf.line(73, 151, 200, 151) #insert a line 

#Pull company highlights text
#import text from file
with open('Company Highlights.txt', 'r') as file:
    company_highlights_text = file.read()
#Replace unsupported characters for FPDF
company_highlights_text = company_highlights_text.replace("’", "'").replace("“", '"').replace("”", '"').replace("–", "-").replace("—", "-")

#Set font for company highlights text
pdf.set_font('Arial','',10)
pdf.set_text_color(0,0,0)
pdf.set_xy(72,154)

#Iterate through lines and apply bold to titles
for i, line in enumerate(company_highlights_text.split('\n')):
    if i % 2 == 0:  # Odd lines (0-based index)
        pdf.set_font('Arial', 'B', 10)  # Bold font
    else:  # Even lines
        pdf.set_font('Arial', '', 10)  # Regular font
    pdf.set_x(72)  # Reset x position to 72 for each line
    pdf.multi_cell(129, 4, line.strip(), align='J')

pdf.add_page()

# === Placeholder Sections ===
pdf.ln(10)
pdf.set_font("Arial", "B", 14)
pdf.cell(0, 10, "Financial Ratios", ln=True)
pdf.set_font("Arial", "", 12)
pdf.multi_cell(0, 10, "[To be generated using financial API functions.]")

pdf.ln(5)
pdf.set_font("Arial", "B", 14)
pdf.cell(0, 10, "DCF Valuation", ln=True)
pdf.set_font("Arial", "", 12)
pdf.multi_cell(0, 10, "[Extracted from Excel - handled by teammate.]")

pdf.ln(5)
pdf.set_font("Arial", "B", 14)
pdf.cell(0, 10, "Commentary", ln=True)
pdf.set_font("Arial", "", 12)
pdf.multi_cell(0, 10, "[To be imported from .txt file.]")

pdf.ln(5)
pdf.set_font("Arial", "B", 14)
pdf.cell(0, 10, "Charts & Price History", ln=True)
pdf.set_font("Arial", "", 12)
pdf.multi_cell(0, 10, "[To be added - stock price vs ASX200 history.]")


# === Output ===
pdf.output("Vicinity Centres Equity Research Report.pdf")