#!/usr/bin/env python

import re
import sys

rgx = re.compile('(\d+)x(\d+)x(\d+)')

with open(sys.argv[1]) as f:
  summa = 0
  for line in f.readlines():
    a,b,c = [ int(i) for i in rgx.split(line)[1:-1] ]
    surface = 2*a*b + 2*a*c + 2*b*c
    extra = min([a*b, a*c, b*c])
    summa += surface + extra

print "Required sheet of wrapping paper: %d" % summa
