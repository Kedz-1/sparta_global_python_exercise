from src.starwars.load import load_json
from src.starwars.write import write_csv
from dotenv import load_dotenv
import os

load_dotenv()
file_path = os.getenv('FILE_PATH')

def convert_to_csv(input_file, output_file):

    data = load_json(input_file)
    response = write_csv(data, output_file)


# print(convert_to_csv(file_path, "characters.csv"))