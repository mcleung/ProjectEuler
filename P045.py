# -*- coding: utf-8 -*-
#==============================================================================
# Triangle, pentagonal, and hexagonal numbers are generated by the following formulae:
#
# Triangle      Tn=n(n+1)/2     1, 3, 6, 10, 15, ...
# Pentagonal    Pn=n(3n−1)/2    1, 5, 12, 22, 35, ...
# Hexagonal     Hn=n(2n−1)      1, 6, 15, 28, 45, ...
# It can be verified that T285 = P165 = H143 = 40755.
# 
# Find the next triangle number that is also pentagonal and hexagonal.
#==============================================================================

class Tri():
    def __init__(self, n=1):
        self.n = n
        self.val = self.GetVal(n)

    def GetVal(self, n):
        return n*(n+1)/2
    
    def Next(self):
        self.n += 1
        self.val = self.GetVal(self.n)
        return self.val

class Pen():
    def __init__(self, n=1):
        self.n = n
        self.val = self.GetVal(n)

    def GetVal(self, n):
        return n*(3*n-1)/2
    
    def Next(self):
        self.n += 1
        self.val = self.GetVal(self.n)
        return self.val

class Hex():
    def __init__(self, n=1):
        self.n = n
        self.val = self.GetVal(n)

    def GetVal(self, n):
        return n*(2*n-1)
    
    def Next(self):
        self.n += 1
        self.val = self.GetVal(self.n)
        return self.val

T = Tri(285)
P = Pen(165)
H = Hex(143)

Tn = T.Next()
Pn = P.Next()
Hn = H.Next()

# Note if you look at T and H series, the H series is every other number in the T series. Thus we can skip calculating the T series and only compare the P and H series.

#while not (Tn==Pn==Hn):
while not (Pn==Hn):

    Small = min(Pn, Hn)
#    Small = min(Tn, Pn, Hn)
#    if Small==Tn:
#        Tn = T.Next() 
    if Small==Pn:
        Pn = P.Next()
    if Small==Hn:
        Hn = H.Next()

print P.n, H.n, Hn
# 31977 27693 1533776805
