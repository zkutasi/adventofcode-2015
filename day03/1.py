#!/usr/bin/env python

with open('input.txt') as f:
  x = 0
  y = 0
  visits = [(x,y)]
  for line in f.readlines():
    for c in line:
      if c == '>':
        x += 1
      elif c == '<':
        x -= 1
      elif c == '^':
        y += 1
      elif c == 'v':
        y -= 1
      visits += [ (x,y) ]

print "Presents given: %s" % len(visits)
print "At least one present gievn: %s" % len(set(visits))
