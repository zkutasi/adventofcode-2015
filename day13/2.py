#!/usr/bin/env python

from collections import defaultdict
from itertools import permutations
import re
import sys

rgx = re.compile('(\S+) would (gain|lose) (\d+) happiness units by sitting next to (\S+).')

rules = defaultdict(dict)
with open(sys.argv[1]) as f:
  for line in f.readlines():
    p1, n1, n2, p2 = rgx.split(line.strip())[1:-1]
    num = int(n2) if n1 == 'gain' else -int(n2)
    rules[p1][p2] = num

for p in rules.keys():
  rules['ME'][p] = 0
  rules[p]['ME'] = 0

class Seat(object):
  def __init__(self, name):
    self.name = name
    self.right = None
    self.left = None
    self.happiness = 0

  def eval(self):
    self.happiness += rules[self.name][self.left.name]
    self.happiness += rules[self.name][self.right.name]

  def __repr__(self):
    return "%s=%d" % (self.name, self.happiness)




allseatings = []
for seating in permutations(rules.keys()):
  seats = [ Seat(person) for person in seating ]
  for s in range(len(seats)):
    if s == len(seats)-1:
      seats[s].left = seats[s-1]
      seats[s].right = seats[0]
    else:
      seats[s].left = seats[s-1]
      seats[s].right = seats[s+1]

    seats[s].eval()
  allseatings += [ seats ]
  #print "%s ---> %d" % (','.join([ str(s) for s in seats ]), sum([ s.happiness for s in seats ]))


print "The best total happiness is: %d" % max([ sum([ s.happiness for s in seats ]) for seats in allseatings ])
