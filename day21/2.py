#!/usr/bin/env python

from itertools import combinations
import sys


class Entity(object):
  def __init__(self, name, hitpoints, damage, armor):
    self.name = name
    self.hitpoints = hitpoints
    self.damage = damage
    self.armor = armor
    self.items = []

  def equip(self, item):
    self.items += [ item ]
    self.damage += item.damage
    self.armor += item.armor

  def __repr__(self):
    return "%s: %d HP, %d/%d" % (self.name, self.hitpoints, self.damage, self.armor)


class Item(object):
  WEAPON = 0
  ARMOR = 1
  RING = 3

  def __init__(self, name, typ, cost, damage, armor):
    self.name = name
    self.type = typ
    self.cost = cost
    self.damage = damage
    self.armor = armor

  def __repr__(self):
    return "%s (%d/%d)" % (self.name, self.damage, self.armor)


shop = [
  Item('Dagger', Item.WEAPON, 8, 4, 0),
  Item('Shortsword', Item.WEAPON, 10, 5, 0),
  Item('Warhammer', Item.WEAPON, 25, 6, 0),
  Item('Longsword', Item.WEAPON, 40, 7, 0),
  Item('Greataxe', Item.WEAPON, 74, 8, 0),
  Item('Leather', Item.ARMOR, 13, 0, 1),
  Item('Chainmail', Item.ARMOR, 31, 0, 2),
  Item('Splintmail', Item.ARMOR, 53, 0, 3),
  Item('Bandedmail', Item.ARMOR, 75, 0, 4),
  Item('Platemail', Item.ARMOR, 102, 0, 5),
  Item('Damage +1', Item.RING, 25, 1, 0),
  Item('Damage +2', Item.RING, 50, 2, 0),
  Item('Damage +3', Item.RING, 100, 3, 0),
  Item('Defense +1', Item.RING, 20, 0, 1),
  Item('Defense +2', Item.RING, 40, 0, 2),
  Item('Defense +3', Item.RING, 80, 0, 3)
]
weapons = []
armors = []
rings = []
for w in [1]:
  weapons += list(combinations([ i for i in shop if i.type == Item.WEAPON ], w))
for a in [0,1]:
  armors += list(combinations([ i for i in shop if i.type == Item.ARMOR ], a))
for r in [0,1,2]:
  rings += list(combinations([ i for i in shop if i.type == Item.RING ], r))


class Game(object):
  def __init__(self):
    boss_hitpoints = None
    boss_damage = None
    boss_armor = None
    with open(sys.argv[1]) as f:
      for line in f.readlines():
        if line.startswith('Hit Points'):
          boss_hitpoints = int(line.split(':')[1].strip())
        if line.startswith('Damage'):
          boss_damage = int(line.split(':')[1].strip())
        if line.startswith('Armor'):
          boss_armor = int(line.split(':')[1].strip())
    self.boss = Entity("Boss", boss_hitpoints, boss_damage, boss_armor)
    self.player = Entity("Player", 100, 0, 0)
    self.opponents = [ self.player, self.boss ]
    self.turn = 0

  def __repr__(self):
    return "%s --- %s" % (str(self.player), str(self.boss))

  def play(self):
    while self.player.hitpoints > 0 and self.boss.hitpoints > 0:
      attacker = self.opponents[self.turn % 2]
      defender = self.opponents[(self.turn % 2) - 1]
      damage = attacker.damage - defender.armor
      if damage < 1:
        damage = 1
      defender.hitpoints -= damage
      self.turn += 1
    if self.player.hitpoints > 0:
      return True
    else:
      return False



leastgold = float('inf')
mostgold = float('-inf')
for weapon in weapons:
  for armor in armors:
    for ring in rings:
      g = Game()
      for w in weapon:
        g.player.equip(w)
      for a in armor:
        g.player.equip(a)
      for r in ring:
        g.player.equip(r)
      won = g.play()
      goldspent = sum([ i.cost for i in g.player.items ])
      if won:
        print "Player WON, spent %d gold" % goldspent
        leastgold = min(leastgold, goldspent)
      else:
        print "Player LOST"
        mostgold = max(mostgold, goldspent)

print "the Least gold spent while winning: %d" % leastgold
print "the Most gold spent while losing: %d" % mostgold
