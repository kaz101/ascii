#! /bin/env python3

import escapecodes
import sys
import time
import random
a = escapecodes.Ansi()

sys.stdout.write(a.effects('bold'))
sys.stdout.write(a.effects('overlined'))
sys.stdout.write(a.effects('underline'))
sys.stdout.write(a.cursor('clr_scr'))
sys.stdout.write(a.cursor('up', 30))
sys.stdout.write(a.cursor('right', 12))

sen_1 = 'First I had Sativa '
sen_2 = 'Then I had Indica '
sen_3 = 'Now I\'m a Hybrid\n\n\n\n'

for i in sen_1:
    sys.stdout.write(a.color('br_green'))
    sys.stdout.write(i)
    sys.stdout.flush()
    time.sleep(0.1)
time.sleep(2)

for i in sen_2:
    sys.stdout.write(a.color('br_red'))
    sys.stdout.write(i)
    sys.stdout.flush()
    time.sleep(0.1)
time.sleep(2)
count = 1

for i in sen_3:
    if count % 2 == 0:
        color = 'br_red'
    else:
        color = 'br_green'
    sys.stdout.write(a.color(color))
    sys.stdout.write(i)
    sys.stdout.flush()
    count += 1

    time.sleep(0.1)
