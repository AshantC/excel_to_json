import PyPDF2
import pandas as pd

# File Path
pdf_file = "Files/pdf/sample_table.pdf"
output_excel = "sample_table_output.xlsx"

# Function to extract text from a PDF
def extract_text_from_pdf(pdf_file):
    text = ""
    with open(pdf_file, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        for page in reader.pages:
            text += page.extract_text()
    return text

# Function to parse text into a table (adjust based on your PDF's structure)
def parse_text_to_table(text):
    lines = text.split("\n")
    data = [line.split() for line in lines] # Split lines into columns by whitespace
    return data

# Extract and process the PDF
try:
    # Extract text from the PDF
    pdf_text = extract_text_from_pdf(pdf_file)
    
    # Parse the extracted text into a table
    table_data = parse_text_to_table(pdf_text)
    
    # Convert to a pandas DataFrame
    df = pd.DataFrame(table_data)
    
    # Save to Excel
    df.to_excel(output_excel, index=False, header=False)
    
except Exception as e:
    print(f"An error occured: {e}")