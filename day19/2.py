#!/usr/bin/env python

from collections import defaultdict
from random import shuffle
import re
import sys
import time

rgx_repl = re.compile('(\S+) => (\S+)')


molecule = None
atoms = set()
replacements = []
with open(sys.argv[1]) as f:
  for line in f.readlines():
    if rgx_repl.match(line.strip()):
      m1, m2 = rgx_repl.split(line.strip())[1:-1]
      replacements += [ (m1, m2) ]
      atoms.add(m1)
    elif line.strip() == '':
      pass
    else:
      molecule = line.strip()



found = False
mol = molecule
steps = 0
while not found:
  changed = False
  for rule in replacements:
      if rule[1] not in mol:
        continue
      mol = mol.replace(rule[1], rule[0], 1)
      changed = True
      steps += 1
      if mol == 'e':
        print "Found it in %d steps" % steps
        found = True
  if not changed:
    changed = False
    print "Shuffling replacement list..."
    shuffle(replacements)
    mol = molecule
    steps = 0
