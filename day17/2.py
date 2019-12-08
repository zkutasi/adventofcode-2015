#!/usr/bin/env python

from itertools import combinations
import sys

containers = []
with open(sys.argv[1]) as f:
  for line in f.readlines():
    containers += [ int(line.strip()) ]

amount = int(sys.argv[2])

solutions = [
  c
  for n in range(1, len(containers)+1)
  for c in combinations(containers, n)
  if sum(c) == amount
]

minsolution = len(min(solutions, key=lambda e: len(e)))
print "Minimum container solution: %d" % minsolution
print "Number of such solutions: %d" % len([ s for s in solutions if len(s) == minsolution ])
