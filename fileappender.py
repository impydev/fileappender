#!/usr/bin/env python

import sys

argv1 = str(sys.argv[1])
argv2 = str(sys.argv[2])
argv3 = int(sys.argv[3])
file = open(argv1, 'a+')

for i in range(argv3):
    file.write(argv2 + '\n')
file.close()
