#!/usr/bin/env python

from collections import defaultdict
from itertools import product
import re
import sys

rgx = re.compile('(\S+): capacity (\S+), durability (\S+), flavor (\S+), texture (\S+), calories (\S+)')


class Ingredient(object):
  def __init__(self, name, cap, dur, fla, txt, cal):
    self.name = name
    self.capacity = cap
    self.durability = dur
    self.flavor = fla
    self.texture = txt
    self.calories = cal


ingredients = {}
with open(sys.argv[1]) as f:
  for line in f.readlines():
    name, cap, dur, fla, txt, cal = rgx.split(line.strip())[1:-1]
    ingredients[name] = Ingredient(name, int(cap), int(dur), int(fla), int(txt), int(cal))
ingredient_names = ingredients.keys()



list_of_amounts = [ a for a in product(range(101), repeat=len(ingredients)) if sum(a) == 100 ]
topscore = float('-inf')
for amounts in list_of_amounts:
  zipped_amounts = zip(ingredient_names, amounts)
  capacity = sum([ value * ingredients[name].capacity for name, value in zipped_amounts ])
  if capacity < 0:
    capacity = 0
  durability = sum([ value * ingredients[name].durability for name, value in zipped_amounts ])
  if durability < 0:
    durability = 0
  flavor = sum([ value * ingredients[name].flavor for name, value in zipped_amounts ])
  if flavor < 0:
    flavor = 0
  texture = sum([ value * ingredients[name].texture for name, value in zipped_amounts ])
  if texture < 0:
    texture = 0
  calories = sum([ value * ingredients[name].calories for name, value in zipped_amounts ])
  score = capacity * durability * flavor * texture
  if score > topscore and calories == 500:
    topscore = score
  #print "Chosing %s, the score is %d" % (zipped_amounts, score)

print "The top score for a 500 calories cookie is: %d" % topscore
