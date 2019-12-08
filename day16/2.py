#!/usr/bin/env python

import re
import sys

rgx = re.compile('Sue (\d+): (\S+): (\d+), (\S+): (\d+), (\S+): (\d+)')


class Sue(object):
  def __init__(self):
    self.children = "?"
    self.cats = "?"
    self.samoyeds = "?"
    self.pomeranians = "?"
    self.akitas = "?"
    self.vizslas = "?"
    self.goldfish = "?"
    self.trees = "?"
    self.cars = "?"
    self.perfumes = "?"

  def __repr__(self):
    return "children=%s, cats=%s, samoyeds=%s, pomeranians=%s, akitas=%s, vizslas=%s, goldfish=%s, trees=%s, cars=%s, perfumes=%s" % (
      self.children, self.cats, self.samoyeds, self.pomeranians, self.akitas, self.vizslas, self.goldfish, self.trees, self.cars, self.perfumes
    )


sues = {}
with open(sys.argv[1]) as f:
  for line in f.readlines():
    num, thing1, value1, thing2, value2, thing3, value3 = rgx.split(line.strip())[1:-1]
    num = int(num)
    sues[num] = Sue()
    setattr(sues[num], thing1, int(value1))
    setattr(sues[num], thing2, int(value2))
    setattr(sues[num], thing3, int(value3))


class ClueType(object):
  EQUAL = 0
  GREATER = 1
  LESS = 2

clues = {
  "children": (3, ClueType.EQUAL),
  "cats": (7, ClueType.GREATER),
  "samoyeds": (2, ClueType.EQUAL),
  "pomeranians": (3, ClueType.LESS),
  "akitas": (0, ClueType.EQUAL),
  "vizslas": (0, ClueType.EQUAL),
  "goldfish": (5, ClueType.LESS),
  "trees": (3, ClueType.GREATER),
  "cars": (2, ClueType.EQUAL),
  "perfumes": (1, ClueType.EQUAL)
}


for suenum, sue in sues.items():
  if all([
    (getattr(sue, cluename) in [cluevalue[0], "?"]) if cluevalue[1] == ClueType.EQUAL else
    (getattr(sue, cluename) > cluevalue[0] or getattr(sue, cluename) == '?') if cluevalue[1] == ClueType.GREATER else
    (getattr(sue, cluename) < cluevalue[0] or getattr(sue, cluename) == '?')
    for cluename, cluevalue in clues.items()
  ]):
    print "Matching Sue found: %d - %s" % (suenum, sue)
    
