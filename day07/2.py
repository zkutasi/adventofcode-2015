#!/usr/bin/env python

import re
import sys

rgx_num = re.compile('^(\d+)$')
rgx_val = re.compile('^(\S+) -> (\S+)$')
rgx_and = re.compile('^(\S+) AND (\S+) -> (\S+)$')
rgx_or  = re.compile('^(\S+) OR (\S+) -> (\S+)$')
rgx_lsh = re.compile('^(\S+) LSHIFT (\d+) -> (\S+)$')
rgx_rsh = re.compile('^(\S+) RSHIFT (\d+) -> (\S+)$')
rgx_not = re.compile('^NOT (\S+) -> (\S+)$')

class Instr(object):
  def __init__(self, dependson, attribute=None):
    self.dep = dependson
    self.attr = int(attribute) if attribute is not None else None
    self.value = None
  def __repr__(self):
    return str(self.getvalue())

class NumValue(Instr):
  def getvalue(self):
    return self.attr

class Value(Instr):
  def getvalue(self):
    if self.value is None:
      self.value = self.dep[0].getvalue()
    return self.value

class And(Instr):
  def getvalue(self):
    if self.value is None:
      self.value = self.dep[0].getvalue() & self.dep[1].getvalue()
    return self.value

class Or(Instr):
  def getvalue(self):
    if self.value is None:
      self.value = self.dep[0].getvalue() | self.dep[1].getvalue()
    return self.value

class LShift(Instr):
  def getvalue(self):
    if self.value is None:
      self.value = self.dep[0].getvalue() << self.attr
    return self.value

class RShift(Instr):
  def getvalue(self):
    if self.value is None:
      self.value = self.dep[0].getvalue() >> self.attr
    return self.value

class Not(Instr):
  def getvalue(self):
    if self.value is None:
      self.value = (~self.dep[0].getvalue()) & (2**16-1)
    return self.value

wires = {}
head = None

with open(sys.argv[1]) as f:
  for line in f.readlines():
    instr = None
    match = rgx_val.match(line.strip())
    if match:
      prov = match.group(2)
      instr = Value([match.group(1)])
      wires[prov] = instr
    match = rgx_and.match(line.strip())
    if match:
      prov = match.group(3)
      instr = And([match.group(1), match.group(2)])
      wires[prov] = instr
    match = rgx_or.match(line.strip())
    if match:
      prov = match.group(3)
      instr = Or([match.group(1), match.group(2)])
      wires[prov] = instr
    match = rgx_lsh.match(line.strip())
    if match:
      prov = match.group(3)
      instr = LShift([match.group(1)], match.group(2))
      wires[prov] = instr
    match = rgx_rsh.match(line.strip())
    if match:
      prov = match.group(3)
      instr = RShift([match.group(1)], match.group(2))
      wires[prov] = instr
    match = rgx_not.match(line.strip())
    if match:
      prov = match.group(2)
      instr = Not([match.group(1)])
      wires[prov] = instr
    #print "Adding provider for wire %s" % prov

wires['b'] = Value(['16076'])

for k,v in wires.items():
  for idx,d in enumerate(v.dep):
    match = rgx_num.match(d)
    if match:
      v.dep[idx] = NumValue([], match.group(1))
    else:
      v.dep[idx] = wires[d]

print "The values are: %s" % wires
print "The value of 'a' is: %s" % wires['a']

