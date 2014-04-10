"""
A unit fraction contains 1 in the numerator. The decimal
representation of the unit fractions with denominators
2 to 10 are given:

1/2	= 	0.5
1/3	= 	0.(3)
1/4	= 	0.25
1/5	= 	0.2
1/6	= 	0.1(6)
1/7	= 	0.(142857)
1/8	= 	0.125
1/9	= 	0.(1)
1/10	= 	0.1
Where 0.1(6) means 0.166666..., and has a 1-digit
recurring cycle. It can be seen that 1/7 has a 6-digit
recurring cycle.

Find the value of d < 1000 for which 1/d contains the
longest recurring cycle in its decimal fraction part.
"""

def nrep(frac):
    rep = 1
    rem = 10%frac
#    print rem
    while not ((rem==1) or (rem==0)):
        rep += 1
        rem = (rem*10) % frac
        if rep > frac:
            return 0
#        print rem
#        pause(1)
    return 0 if rem==0 else rep

maxrep = 0
for ii in range(1,1001):
    n = nrep(ii)
    if n > maxrep:
        maxrep = n
        maxii = ii

print maxii
#983