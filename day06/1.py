#!/usr/bin/env python

import re
import sys

rgx = re.compile('(.*) (\d+),(\d+) through (\d+),(\d+)')

grid = [ [ 0 for x in range(1000) ] for y in range(1000) ]


with open(sys.argv[1]) as f:
  for line in f.readlines():
    instr, x0,y0, x1,y1 = rgx.split(line)[1:-1]
    for x in range(int(x0), int(x1)+1):
      for y in range(int(y0), int(y1)+1):
        if instr == 'turn on':
          grid[x][y] = 1
        elif instr == 'turn off':
          grid[x][y] = 0
        elif instr == 'toggle':
          grid[x][y] = (grid[x][y] + 1) % 2

print "Ligths ON: %d" % len([ light for sublist in grid for light in sublist if light == 1 ])
