#!/usr/bin/env python

import hashlib

myinput = "bgvyzdsv"

md5hash = ""
num = -1
while not md5hash.startswith('00000'):
  num += 1
  md5hash = hashlib.md5(myinput + str(num)).hexdigest()

print "This first number that satisfies: %d" % num
