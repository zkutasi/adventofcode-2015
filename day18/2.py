#!/usr/bin/env python

import sys

w = None
h = None
lights = []
with open(sys.argv[1]) as f:
  for line in f.readlines():
    lights += [ list(line.strip()) ]

w = len(lights[0])
h = len(lights)

def stuck(lights):
  for x in [0, len(lights)-1]:
    for y in [0, len(lights[0])-1]:
      lights[x][y] = '#'


stuck(lights)
steps = int(sys.argv[2])

for s in range(steps):
  newlights = []
  for x in range(len(lights)):
    newlights += [ list(lights[x]) ]

  for x in range(len(lights)):
    for y in range(len(lights[0])):
      neighbors = []
      for i in range(x-1, x+2):
        for j in range(y-1, y+2):
          if i>=0 and j>=0 and i<h and j<w and (i,j) != (x,y):
            neighbors += [ lights[i][j] ]
      if lights[x][y] == '#':
        newlights[x][y] = '#' if len([ n for n in neighbors if n == '#' ]) in [2,3] else '.'
      else:
        newlights[x][y] = '#' if len([ n for n in neighbors if n == '#' ]) == 3 else '.'

  lights = newlights
  stuck(lights)
  #print "After %d step:" % (s+1)
  #print_lights(lights)
  print "Lights are on after step %d: %d" % (s+1, len([ lights[x][y] for x in range(h) for y in range(w) if lights[x][y] == '#' ]))

