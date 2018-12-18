#!/usr/bin/env python

with open('input.txt') as f:
  sx = 0
  sy = 0
  rsx = 0
  rsy = 0
  svisits = [(sx,sy)]
  rsvisits = [(rsx,rsy)]
  robosanta = False
  for line in f.readlines():
    for c in line:
      if c == '>':
        if robosanta:
          rsx += 1
        else:
          sx += 1
      elif c == '<':
        if robosanta:
          rsx -= 1
        else:
          sx -= 1
      elif c == '^':
        if robosanta:
          rsy += 1
        else:
          sy += 1
      elif c == 'v':
        if robosanta:
          rsy -= 1
        else:
          sy -= 1
      if robosanta:
        svisits += [ (rsx,rsy) ]
      else:
        rsvisits += [ (sx,sy) ]
      robosanta = not robosanta

#print "Presents given: %s" % len(visits)
print "At least one present gievn: %s" % len(set(svisits + rsvisits))
