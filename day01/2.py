#!/usr/bin/env python

import sys

with open(sys.argv[1]) as f:
  for line in f.readlines():
    floor = 0
    cnum = 1
    for c in line:
      if c == '(':
        floor += 1
      if c == ')':
        floor -= 1
      if floor == -1:
        print "Step to get you to floor -1: %d" % cnum
        break
      cnum += 1
        
