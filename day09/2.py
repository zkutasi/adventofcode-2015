#!/usr/bin/env python

import re

rgx = re.compile('^(\S+) to (\S+) = (\d+)$')

cities = set([])
distances = {}
with open('input.txt') as f:
  for line in f.readlines():
    frm, to, dist = rgx.split(line)[1:-1]
    cities.add(to)
    cities.add(frm)
    distances[(frm, to)] = int(dist)
    distances[(to, frm)] = int(dist)
cities = list(cities)


def travel(vis_cities, dist):
  travels = []
  for c in [ city for city in set(cities)-set(vis_cities)]:
    if len(vis_cities) == 0:
      add_dist = 0
    else:
      add_dist = distances[vis_cities[-1], c]
    travels += travel(vis_cities + [c], dist + add_dist)
  if len(travels) == 0:
    travels = [(vis_cities, dist)]
  return travels


travels = travel([], 0)
print "Shortest Travel: %s --> %s" % min(travels, key=lambda (c,d): d)
print "Longest Travel: %s --> %s" % max(travels, key=lambda (c,d): d)
