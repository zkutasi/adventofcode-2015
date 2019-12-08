#!/usr/bin/env python

import re
import sys

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


next_molecules = set()
for rule in replacements:
  findings = [ m.start() for m in re.finditer(rule[0], molecule) ]
  for f in findings:
    before = molecule[:f]
    after = molecule[f:]
    after = after.replace(rule[0], rule[1], 1)
    next_molecules.add(before + after)


print "Number of new molecules: %d" % len(next_molecules)
