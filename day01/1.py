#!/usr/bin/env python

import sys

with open(sys.argv[1]) as f:
  for line in f.readlines():
    print "End floor: %d" % (line.count('(')-line.count(')'))
