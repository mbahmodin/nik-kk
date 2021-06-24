import json
import random
import os

dir_path = os.path.dirname(os.path.realpath(__file__))
here = json.load(open(dir_path + "/" + 'data.json'))
x = random.choice(here).split('|')
print("Jumlah NIK & KK :", len(here))
print("NIK : " + x[0] + "\nKK  : " + x[1])
