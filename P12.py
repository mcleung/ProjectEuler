# -*- coding: utf-8 -*-
#===============================================================================
# The sequence of triangle numbers is generated by adding the natural numbers.
# So the 7th triangle number would be 1 + 2 + 3 + 4 + 5 + 6 + 7 = 28.
# The first ten terms would be:
# 1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...
# Let us list the factors of the first seven triangle numbers:
#  1: 1
#  3: 1,3
#  6: 1,2,3,6
# 10: 1,2,5,10
# 15: 1,3,5,15
# 21: 1,3,7,21
# 28: 1,2,4,7,14,28
# We can see that 28 is the first triangle number to have over five divisors.
# What is the value of the first triangle number to have over five hundred
# divisors?
#===============================================================================
def numdiv(n):
    c=2
#    print 'divisors of', n
    for ii in range(2,int(n**0.5+1)):
#        print 'checking', ii
        if n%ii==0:
#            print 'is', ii
            c += 2
    return c

for i in xrange(15000):
    n = i * (i+1) / 2
    d = numdiv(n)
    # print i, n, d
    # if i%100==0:
    #     print i
    if d > 500:
        break

print n


