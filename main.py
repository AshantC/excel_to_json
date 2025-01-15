import os
from lib.file_converter import FileConverter
from dotenv import load_dotenv
import click
import uvicorn

@click.command()
@click.option('--mode', type=click.Choice(['api', 'manual'], case_sensitive=False,), help="Run the app in 'api' or 'manual' mode.")



def main(mode):
    # Load environment variables from .env
    load_dotenv(dotenv_path='.local.properties', override=True)
    
    # Get input and output directories from the environment variables
    input_dir = os.getenv("SOURCE_DIR")
    output_dir = os.getenv("OUTPUT_DIR")

    os.makedirs(input_dir, exist_ok=True)
    os.makedirs(output_dir, exist_ok=True)
    
    # Use match expression to handle different modes
    match mode:
        case 'api':
            print("Running the API mode...")
            uvicorn.run('lib.fast_api:app', reload=True)
        
        case 'manual':
            print(f"Running the Manual mode with input: {input_dir} and {output_dir}...")
            app = FileConverter()
            app.conversion(input_dir, output_dir)
            # app.file_name(input_dir)

if __name__ == "__main__":
    main()