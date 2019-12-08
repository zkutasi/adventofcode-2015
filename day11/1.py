#!/usr/bin/env python

from itertools import groupby
import sys
import time

pwd = None
with open(sys.argv[1]) as f:
  for line in f.readlines():
    pwd = list(line.strip())

alphabet = 'abcdefghijklmnopqrstuvwxyz'
alphabet2 = 'abcdefghijklmnopqrstuvwxyz_'

def inc_pwd(pwd):
  newpwd = list(pwd)
  carrypos = -1
  newpwd[carrypos] = alphabet2[alphabet2.index(newpwd[carrypos]) + 1]
  while newpwd[carrypos] == '_':
    newpwd[carrypos] = 'a'
    carrypos -= 1
    newpwd[carrypos] = alphabet2[alphabet2.index(newpwd[carrypos]) + 1]
    if newpwd[carrypos] in 'iol':
      newpwd[carrypos] = alphabet2[alphabet2.index(newpwd[carrypos]) + 1]
  return newpwd


print "Original password: %s" % pwd


incrstraights = []
for i in range(len(alphabet)-2):
  incrstraights += [ alphabet[i:i+3] ]

for s in 'iol':
  try:
    index = pwd.index(s)
    pwd[index] = chr(ord(s)+1)
    for i in range(index+1, len(pwd)):
      pwd[i] = 'a'
  except ValueError:
    pass

while True:
  pwd = ''.join(inc_pwd(pwd))
  if any([ (s in pwd) for s in incrstraights ]) and \
     all([ (s not in pwd) for s in 'iol' ]):
    gr = [ list(g) for k,g in groupby(pwd) ]
    if len(set([ ''.join(g) for g in gr if len(g) == 2 ])) >= 2:
      break


print "New password: %s" % pwd
