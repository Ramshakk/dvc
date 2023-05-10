# my_script.py

import random

with open("output.txt", "w") as f:
    f.write(str(random.randint(0, 100)))
