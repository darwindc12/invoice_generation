# Invoice Generator
This script generates invoices from Excel files in the invoice directory and saves the resulting PDFs in the PDFs directory.

# Requirements
- fpdf library for creating PDFs
- pandas library for working with Excel files
- glob library for searching for files in a directory
- openpyxl library for working with Excel files
- pathlib library for manipulating file paths

# Usage
- Place Excel files in the invoice directory. The file name should be in the format of invoice-number-date.xlsx
- Run the script using python scriptname.py
- The resulting PDFs will be in the PDFs directory, with the same name as the Excel file.
Customization
- You can change the company name and logo by replacing the pythonhow.png file and updating the pdf.cell(w=25, h=8, txt="PythonHow", align="L") line with your desired name.
- You can adjust the format and layout of the PDF by editing the fpdf commands in the script.

# Note
-The script assumes that the excel files have 4 columns named product_id, product_name, amount_purchased, price_per_unit and total_price, any other columns will cause the script to fail.
- The script assumes that the Excel files have one sheet named Sheet 1
- The script assumes that the PDFs will be saved in the PDFs directory, if the directory doesn't exist it will be created.
- The script assumes that the invoice number and date is separated by - in the file name.
