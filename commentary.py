from fpdf import FPDF

pdf = FPDF()
pdf.add_page()

with open("example_files/ALDcommentary.txt", "r") as file:
    commentary = file.read()

print(commentary)

