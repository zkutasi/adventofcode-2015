#!/usr/bin/env python

import sys


sumlength = 0
sumencoded = 0

with open(sys.argv[1]) as f:
  for line in [ l.strip() for l in f.readlines() ]:
    sumlength += len(line)
    encodedlength = len(line) + line.count('\\') + line.count('"') + 2
    sumencoded += encodedlength
    print "%s ---> length: %s, encodedlength: %s" % (line, len(line), encodedlength)

print "The answer is: %d" % (sumencoded-sumlength)
