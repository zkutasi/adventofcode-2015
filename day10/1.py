#!/usr/bin/env python

from itertools import groupby
import sys

num = 1113222113
for i in range(40):
  newnum = ''
  for k, g in groupby(str(num)):
    newnum += str(len(list(g)))
    newnum += k
  num = int(newnum)

print "Result: %d" % len(str(num))
