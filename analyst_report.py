from fpdf import FPDF
# Demonstrate cursor movement

pdf = FPDF()
pdf.add_page()

# === Title and Header ===
pdf.set_font("Arial", "B", 16)
pdf.cell(0, 10, "Equity Research Report: [Company Name]", ln=True, align="C")

pdf.set_font("Arial", "", 12)
pdf.cell(0, 10, "Ticker: ASX:[TICKER]", ln=True)
pdf.cell(0, 10, "Date: April 2025", ln=True)

# === Executive Summary with spacing ===
pdf.ln(10)
pdf.set_font("Arial", "B", 14)
pdf.cell(0, 10, "Executive Summary", ln=True)
pdf.set_font("Arial", "", 12)
pdf.multi_cell(0, 10, "This report outlines [Company Name]'s financial position, valuation, and future outlook. More detail to follow below.")

# === Inline Text Example using write() ===
pdf.ln()
pdf.set_font("Arial", "", 12)
pdf.write(8, "This report uses ")
pdf.set_font("Arial", "B", 12)
pdf.write(8, "inline bold formatting ")
pdf.set_font("Arial", "", 12)
pdf.write(8, "and custom styles.\n")

# === Colored Alert ===
pdf.set_text_color(255, 0, 0)
pdf.cell(0, 10, "Important: Valuation is based on assumptions and may differ.", ln=True)
pdf.set_text_color(0)

# === Absolute Positioned Note ===
pdf.text(10, 110, "Note placed at (10, 110) using text().")

# === Custom Vertical Spacing Demo ===
pdf.ln(10)
pdf.cell(0, 10, "Line 1", 0, 1)
pdf.cell(0, 10, "Line 2 - no spacing", 0, 1)
pdf.ln(10)  # 10mm vertical gap
pdf.cell(0, 10, "Line 3 - after 10mm space", 0, 1)
pdf.ln()
pdf.cell(0, 10, "Line 4 - after default line height", 0, 1)

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

pdf.ln(5)
pdf.set_font("Arial", "B", 14)
pdf.cell(0, 10, "Web-Scraped Table or Image", ln=True)
pdf.set_font("Arial", "", 12)
pdf.multi_cell(0, 10, "[To be scraped from a relevant source or company site.]")

# === Summary ===
pdf.ln(10)
pdf.set_font("Arial", "B", 14)
pdf.cell(0, 10, "Summary & Notes", ln=True)
pdf.set_font("Arial", "", 12)
pdf.multi_cell(0, 10, """This report uses fpdf's sequential, cursor-based structure:
1. Set formatting (font, color)
2. Add content using cell(), multi_cell(), write(), or text()
3. Use ln() or set_y() for spacing
4. Reset formatting when switching styles
""")

# === Output ===
pdf.output("analyst_report.pdf")