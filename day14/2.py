#!/usr/bin/env python

import re
import sys

rgx = re.compile('(\S+) can fly (\d+) km/s for (\d+) seconds, but then must rest for (\d+) seconds.')



class Deer(object):
  FLY = 0
  REST = 1

  def __init__(self, name, speed, flytime, resttime):
    self.name = name
    self.speed = speed
    self.flytime = flytime
    self.resttime = resttime
    self.timer = 0
    self.distance = 0
    self.state = Deer.FLY
    self.score = 0

  def go(self):
    self.timer += 1
    if self.state == Deer.FLY:
      self.distance += self.speed
      if self.timer == self.flytime:
        self.state = Deer.REST
        self.timer = 0
    else:
      if self.timer == self.resttime:
        self.state = Deer.FLY
        self.timer = 0

  def __repr__(self):
    return "%s=%d[%d] (%s)" % (self.name, self.distance, self.score, 'Flying' if self.state == Deer.FLY else 'Resting')



reindeer = {}
with open(sys.argv[1]) as f:
  for line in f.readlines():
    name, speed, flytime, resttime = rgx.split(line.strip())[1:-1]
    reindeer[name] = Deer(name, int(speed), int(flytime), int(resttime))



time = int(sys.argv[2])
for t in range(time):
  for name, deer in reindeer.items():
    deer.go()
  winningdist = max([ r.distance for r in reindeer.values() ])
  for name, deer in reindeer.items():
    if deer.distance == winningdist:
      deer.score += 1
  print "After %d seconds, race result is: %s" % (t+1, ', '.join([ str(r) for r in reindeer.values() ]))
