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
    for k,v in obj.items():
      s += get_sum(v)
  elif isinstance(obj, list):
    for e in obj:
      s += get_sum(e)
  elif isinstance(obj, int):
    s += obj
  else:
    "We missed something..."
  return s


summa = get_sum(data)
print "The sum of all numbers is: %d" % summa
