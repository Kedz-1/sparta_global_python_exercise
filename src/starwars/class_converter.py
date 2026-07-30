from load import load_json
from write import write_csv
#from main import convert_to_csv



class StarWarsConverter():

    def __init__(self, input_file, output_file):
        self.input_file = input_file
        self.output_file = output_file


    def load_json(self):
        return load_json(self.input_file)


    def write_csv(self, data):
        write_csv(data, self.output_file)


    def convert_to_csv(self):
        data = self.load_json()
        self.write_csv(data)

