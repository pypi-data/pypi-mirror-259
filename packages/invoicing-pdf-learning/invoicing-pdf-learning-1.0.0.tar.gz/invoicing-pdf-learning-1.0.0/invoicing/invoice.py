import os

import pandas as pd
import glob
from fpdf import FPDF
from pathlib import Path


def generate(invoices_path, pdfs_path, image_path, product_id, product_name,
             amount_purchased, price_per_unit, total_price):
    """
    This function converts Excel files into PDF invoices.
    :param invoices_path:
    :param pdfs_path:
    :param image_path:
    :param product_id:
    :param product_name:
    :param amount_purchased:
    :param price_per_unit:
    :param total_price:
    :return:
    """
    filepaths = glob.glob(f"{invoices_path}/*.xlsx")

    for filepath in filepaths:
        df = pd.read_excel(filepath, sheet_name="Sheet 1")
        pdf = FPDF(orientation="P", unit="mm", format="A4")

        pdf.add_page()

        filename = Path(filepath).stem
        invoice_nr, date = filename.split("-")

        pdf.set_font(family="Times", size=16, style="B")
        pdf.cell(w=50, h=0, txt=f"Invoice nr. {invoice_nr}", ln=1, align="L")

        pdf.set_font(family="Times", size=16, style="B")
        pdf.cell(w=50, h=16, txt=f"Date: {date}", ln=1, align="L")

        # Table header
        columns = df.columns
        columns = [item.replace("_", " ").title() for item in columns]

        pdf.set_font(family="Times", size=10, style="B")
        pdf.cell(w=30, h=6, txt=columns[0], align="L", border=1)
        pdf.cell(w=70, h=6, txt=columns[1], align="L", border=1)
        pdf.cell(w=35, h=6, txt=columns[2], align="L", border=1)
        pdf.cell(w=30, h=6, txt=columns[3], align="L", border=1)
        pdf.cell(w=25, h=6, txt=columns[4], align="L", border=1, ln=1)

        # Table content
        for index, row in df.iterrows():
            pdf.set_font(family="Times", size=10)
            pdf.cell(w=30, h=6, txt=str(row[product_id]), align="L", border=1)
            pdf.cell(w=70, h=6, txt=row[product_name], align="L", border=1)
            pdf.cell(w=35, h=6, txt=str(row[amount_purchased]), align="L",
                     border=1)
            pdf.cell(w=30, h=6, txt=str(row[price_per_unit]), align="L",
                     border=1)
            pdf.cell(w=25, h=6, txt=str(row[total_price]), align="L",
                     border=1, ln=1)

        # Table total price
        total_sum = df[total_price].sum()
        pdf.set_font(family="Times", size=10)
        pdf.cell(w=30, h=6, txt="", align="L", border=1)
        pdf.cell(w=70, h=6, txt="", align="L", border=1)
        pdf.cell(w=35, h=6, txt="", align="L", border=1)
        pdf.cell(w=30, h=6, txt="", align="L",border=1)
        pdf.cell(w=25, h=6, txt=str(total_sum), align="L", border=1, ln=1)

        # total price text
        pdf.cell(w=25, h=6, txt="", align="L", ln=1)
        pdf.set_font(family="Times", size=10, style="B")
        pdf.cell(w=60, h=6, txt=f"The total due amount is {total_sum} Euros.",
                 align="L", ln=1)

        # company
        pdf.cell(w=19, h=6, txt="PythonHow", align="L")
        pdf.image(image_path, w=8)

        if not os.path.exists(pdfs_path):
            os.makedirs(pdfs_path)
        pdf.output(f"{pdfs_path}/{filename}.pdf")
