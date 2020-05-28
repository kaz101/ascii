#! /bin/env python3
import time
import random

for i in range(100):
    print()

for i in range(2000):
    randnum = random.randint(0, 80)
    print(('0' * randnum) + '*' + '0' * (79 - randnum))
    randnum += 1
    print(('0' * randnum) + '_' + '0' * (79 - randnum))
    randnum -=1
    print(('0' * randnum) + '*' + '0' * (79 - randnum))
    time.sleep(.1)
