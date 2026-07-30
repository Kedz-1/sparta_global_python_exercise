import json
import os

def load_json(file_path):

    new_list = []

    files = [file for file in os.listdir(file_path) if file.endswith(".json")]

    for file in files:

        with open(f'{file_path}/{file}', "r") as f:
            data = json.load(f)
            new_list += data
    return new_list

# print(load_json(file_path))