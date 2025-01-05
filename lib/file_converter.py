import pandas as pd
import os


class FileConverter: 
    def __init__(self):...
        
    def conversion(self, source_dir:str, output_dir:str):
        # Excel file (source file)
        excel_file = "example_excel_file.xlsx"
        excel_file_path = os.path.join(source_dir, excel_file) # Excel file with full path
        sheet_name = 0
        
        # Json file (Output file)
        output_file = "example_json_file.json"
        output_file_path = os.path.join(output_dir, output_file) # Json fill with full path
        
        # Read the Excel File
        df = pd.read_excel(excel_file_path, sheet_name=sheet_name)
        
        # Convert Dataframe to Json
        df.to_json(output_file_path, orient="records", indent=4)
        
        print(f"Success")
   
# def file_converter(source_dir, output_dir)->FileConverter:
#     return FileConverter().file_converter(source_dir, output_dir)

# file_converter(source_dir, output_dir)

def get_conversion(source_dir, output_dir)->FileConverter:
    return FileConverter().conversion(source_dir, output_dir)

