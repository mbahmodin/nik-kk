import json
import random

here = json.load(open('data.json'))
x = random.choice(here).split('|')
print("Jumlah NIK & KK :", len(here))
print("NIK : " + x[0] + "\nKK  : " + x[1])
