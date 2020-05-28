#! /bin/env python3

import sys
import escapecodes
import time
import random

a = escapecodes.Ansi()
file = sys.argv[1]

def open_file(file):
    with open(file) as file:
        text = file.read()
        return text
text = open_file(file)

def print_to_screen(text):
    sys.stdout.write(a.cursor('clr_scr'))
    sys.stdout.write(a.cursor('left',1000))
    sys.stdout.write(a.cursor('up',100))

    for i in text:
        sys.stdout.write(i)
        sys.stdout.flush()
        if i == ',':
            time.sleep(0.3)
        elif i == '.':
            time.sleep(0.7)
        else:
            time.sleep(.1)

print_to_screen(text)
