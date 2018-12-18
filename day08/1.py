#!/usr/bin/env python

sumlength = 0
summemory = 0
with open('input.txt') as f:
  for line in [ l.strip() for l in f.readlines() ]:
    sumlength += len(line)
    memorylength = len(eval(line))
    summemory += memorylength
    print "%s ---> length: %s, memorylength: %s" % (line, len(line), memorylength)

print "The answer is: %d" % (sumlength-summemory)
