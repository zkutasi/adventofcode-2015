#!/usr/bin/env python

import math
import sys
import time

num = int(sys.argv[1])


def get_divisors(n):
  d = set()
  d.add(1)
  d.add(n)
  if n % 2 == 0:
    start = 2
    jump = 1
  else:
    start = 3
    jump = 2
  for i in xrange(start,int(math.sqrt(n))+1, jump):
    if n % i == 0:
      d.add(i)
      d.add(n/i)
  return d


house = 1
while True:
  presents = sum([ d*10 for d in get_divisors(house) ])
  if presents >= num:
    print "House %d got %d presents." % (house, presents)
    break
  house += 1
