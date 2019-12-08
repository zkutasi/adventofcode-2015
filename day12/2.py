#!/usr/bin/env python

import json
import sys

data = None
with open(sys.argv[1]) as f:
  for line in f.readlines():
    data = json.loads(line)


def get_sum(obj):
  s = 0
  if isinstance(obj, dict):
    s2 = 0
    for k,v in obj.items():
      if k == 'red' or v == 'red':
        return s
      s2 += get_sum(v)
    s += s2
  elif isinstance(obj, list):
    for e in obj:
      s += get_sum(e)
  elif isinstance(obj, int):
    s += obj
  return s


summa = get_sum(data)
print "The sum of all numbers is: %d" % summa
