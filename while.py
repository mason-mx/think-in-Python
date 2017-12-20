#!/usr/bin/python
# -*- coding: UTF-8 -*-

x = 6
y = 5


while y:
    x = 6 #x=0 forever if without this line, so the x*y output is impossible
    while x:
        print x,y
        x = x - 1
    print y, " sss"
    y = y - 1

i = 2
while(i < 100):
   j = 2
   while(j <= (i/j)):
      if not(i%j): break
      #print j
      j = j + 1
   if (j > i/j) : print i, " 是素数"
   i = i + 1

print "Good bye!"
