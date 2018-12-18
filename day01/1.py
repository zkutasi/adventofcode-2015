#!/usr/bin/env python

with open('input.txt') as f:
  for line in f.readlines():
    print "End floor: %d" % line.count('(')-line.count(')')
