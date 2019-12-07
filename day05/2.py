#!/usr/bin/env python

import sys


def twice(line):
  for i in range(0, len(line)-1):
    if line.count(line[i:i+2]) > 1:
      print "double in %s: %s" % (line, line[i:i+2])
      return True
  return False

def between(line):
  for i in range(0, len(line)-2):
    if line[i] == line[i+2]:
      return True
  return False

nice = 0
naughty = 0

with open(sys.argv[1]) as f:
  for line in [ l.strip() for l in f.readlines()]:
    isnice = all([
                   twice(line),
                   between(line)
                ])
    if isnice:
      nice += 1
      print line
    else:
      naughty += 1

print "Naughties: %d" % naughty
print "Nices: %d" % nice
