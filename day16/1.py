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


clues = {
  "children": 3,
  "cats": 7,
  "samoyeds": 2,
  "pomeranians": 3,
  "akitas": 0,
  "vizslas": 0,
  "goldfish": 5,
  "trees": 3,
  "cars": 2,
  "perfumes": 1
}


for suenum, sue in sues.items():
  if all([
    getattr(sue, cluename) in [cluevalue, "?"]
    for cluename, cluevalue in clues.items()
  ]):
    print "Matching Sue found: %d - %s" % (suenum, sue)
    
