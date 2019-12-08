#!/usr/bin/env python

def next_num(s):
  result = []
  i = 0
  while i < len(s):
    count = 1
    while i+1 < len(s) and s[i] == s[i+1]:
      i += 1
      count += 1
    result += [ str(count) + s[i] ]
    i += 1
  return ''.join(result)


num = '1113222113'
for i in range(50):
  num = next_num(num)
  print "Result after %d rounds: %d" % (i+1, len(str(num)))
  


print "Result: %d" % len(str(num))
