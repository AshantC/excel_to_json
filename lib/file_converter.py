import pandas as pd
import os
import logging
from .logs import log_handler
from colorama import Style, Fore

class FileConverter: 
    def __init__(self):
        self.log_handler = log_handler()
        
    def file_name(self, input_dir):
        all_files = []
        try:
            if not os.path.exists(input_dir):
                print(f"Path does not exits: {input_dir}")
            else:
                all_files = [os.path.splitext(file)[0] for file in os.listdir(input_dir)]
            logging.info(f"{all_files} generated successfully.")
        except Exception as e:
            print(f"Something went wrong on all_files: {e}")
            logging.error(f"Something went wrong on all_files : {e}")
        
    
        
    def conversion(self, source_dir:str, output_dir:str):
        all_files = []
        try:
            os.makedirs(output_dir, exist_ok=True)
            if not os.path.exists(source_dir):
                print(f"File does not exist")
            else:
                all_files = [os.path.splitext(file)[0] for file in os.listdir(source_dir)]
            
            # Read excel from list
            for file in all_files:
                excel_file = os.path.join(source_dir, file + ".xlsx")
                df = pd.read_excel(excel_file, sheet_name=0)
                
                # Output file
                output_file = os.path.join(output_dir, file + ".json")
                df.to_json(output_file, orient='records',indent=4)
                logging.info(f"File {file} converted successfully.")
                print(Fore.GREEN + f"{file} is converted to {output_file} successfully." + Style.RESET_ALL)
        except Exception as e:
            print(f"File not found: {e}")
            logging.error(f"Something went wrong in conversion: {e}")


def get_converter()->FileConverter:
    return FileConverter()
    
