import csv
from src.starwars.load import load_json
#from dotenv import load_dotenv


def write_csv(data, output_file_path):

    headers = list(data[0].keys())

    with open(output_file_path, "w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=headers )

        writer.writeheader()
        writer.writerows(data)

    return None

