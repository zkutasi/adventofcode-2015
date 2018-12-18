#!/usr/bin/env python

import re

rgx = re.compile('(\d+)x(\d+)x(\d+)')

with open('input.txt') as f:
  summa = 0
  for line in f.readlines():
    a,b,c = [ int(i) for i in rgx.split(line)[1:-1] ]
    summa += min([2*(a+b), 2*(a+c), 2*(b+c)]) + a*b*c

print "Required ribbon: %d" % summa
