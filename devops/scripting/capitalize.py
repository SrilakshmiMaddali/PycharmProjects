#!/usr/bin/env python3

import sys
for line in sys.stdin:
    print(line.strip().capitalize())


#cat newfile.txt | ./capitalize.py