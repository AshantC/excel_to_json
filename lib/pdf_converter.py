import PyPDF2
import pandas as pd
from docx import Document

# File paths
pdf_file = "Files/pdf/Literature.pdf"
output_excel = "Files/Output/literature_output.xlsx"
output_file = "Files/Output/literature.docs"

# Function to extract text from pdf
def extract_text_from_pdf(pdf_file):
    text = ""
    with open(pdf_file, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        for page in reader.pages:
            text += page.extract_text()

    print("----------------- extract_text_from_pdf --------------------")
    print(text)
    return text

def pdf_to_text(pdf_file, output_file):
    reader = PyPDF2.PdfReader(pdf_file)
    with open(output_file, 'w', encoding='utf-8') as f:
        for page in reader.pages:
            f.write(page.extract_text() + '\n')
            
pdf_to_text(pdf_file, output_file)
