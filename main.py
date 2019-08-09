from pprint import pprint
import json

with open('./data/banks/ABBank/1/bctt.json') as json_file:
    data = json.load(json_file)
    pprint(data[0])