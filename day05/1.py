#!/usr/bin/env python

import sys

nice = 0
naughty = 0

with open(sys.argv[1]) as f:
  for line in f.readlines():
    isnice = all([
                  len([ c for c in line if c in 'aeiou' ]) >= 3,
                  len([ (c1, c2) for (c1, c2) in zip(line, line[1:]) if c1 == c2 ]) > 0,
                  ( 'ab' not in line and
                    'cd' not in line and
                    'pq' not in line and
                    'xy' not in line)
                ])
    if isnice:
      nice += 1
    else:
      naughty += 1

print "Naughties: %d" % naughty
print "Nices: %d" % nice
