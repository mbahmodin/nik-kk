import json
import random
import os

dir_path = os.path.dirname(os.path.realpath(__file__))
json_data = json.load(open(dir_path + "/" + 'data.json'))
output_numbers = random.choice(json_data).split('|')
print("Numbers of NIK & KK :", len(json_data))
print("NIK : " + output_numbers[0] + "\nKK  : " + output_numbers[1])