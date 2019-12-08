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

print "Solutions: %s" % solutions
print "Number of solutions: %d" % len(solutions)
