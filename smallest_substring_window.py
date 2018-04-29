from collections import defaultdict
import collections
import sys

import pdb

def smallest(s1, s2):
    assert s2 != ''
    d = defaultdict(int)
    nneg = [0]  # number of negative entries in d
    def incr(c):
        d[c] += 1
        if d[c] == 0:
            nneg[0] -= 1
    def decr(c):
        if d[c] == 0:
            nneg[0] += 1
        d[c] -= 1
    for c in s2:
        decr(c)
    minlen = len(s1) + 1
    j = 0
    for i in range(len(s1)):
        while nneg[0] > 0:
            if j >= len(s1):
                return minlen
            incr(s1[j])
            j += 1
        minlen = min(minlen, j - i)
        decr(s1[i])
    return minlen


print(smallest("cabeca", "cae"))

def newShortest(subString, string):
  myChars = set(subString)
  smallest = ""
  current={}
  for i, char in enumerate(string):
    if char in myChars:
      current[char] = i
      if len(current) == len(myChars):
        temp = string[current[min(current,key=current.get)]:current[max(current,key=current.get)]+1]
        if len(temp) < len(smallest) or len(smallest) == 0:
          smallest = temp

  return smallest
  print(smallest)


print(newShortest("cabeca", "cae"))


import time

args = ["hello","I would like to all over you hehhhhhkkkkkkkkkklo"]

def timeIt(func,args):
  then = time.time()
  for _ in range(10000):
    func(*args)
  print("{} timing: {:.2f}".format(func.__name__, time.time()-then))

timeIt(newShortest,args)
