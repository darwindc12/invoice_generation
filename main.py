from fpdf import FPDF
import pandas
import glob
import openpyxl
import pathlib

filepaths = glob.glob("invoice/*.xlsx")


for filepath in filepaths:
    df = pandas.read_excel(filepath, sheet_name="Sheet 1")
    pdf = FPDF(orientation="P", unit='mm', format="A4")
    pdf.add_page()
    filename = pathlib.Path(filepath).stem
    nv = filename.split("-")[0]
    pdf.set_font(family="Times", style="B", size=16)
    pdf.cell(w=50, h=8, txt=f"Invoice nr. {nv}", align="L")
    pdf.output(f"PDFs/{filename}.pdf")

