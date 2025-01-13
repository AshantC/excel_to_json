import pandas as pd
import os
import logging
from .logging_app import log_handler

class FileConverter: 
    def __init__(self):
        self.log_handler = log_handler()
        
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
        logging.info(f"{excel_file} is converted into {output_file} successfully")


def get_converter()->FileConverter:
    return FileConverter()
    
