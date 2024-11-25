import pdfplumber
import pandas as pd

def extract_main_table(pdf_path):
    """Extract the main results table from the paper."""
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            tables = page.extract_tables()
            if tables:
                # Assume the first table is the main one
                return pd.DataFrame(tables[0][1:], columns=tables[0][0])
    return None
