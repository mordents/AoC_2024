#Safe reports 
# Levels all increasing or all decreasing
#Any two adjacent levels differ by at least one and at most three.
import sys
from collections import defaultdict, Counter
infile = 'AoC2input.txt'
D = open(infile).read().strip()

def is_good(xs):
    inc_or_dec = (xs==sorted(xs) or xs==sorted(xs,reverse=True)) #use sorted function to determine if increasing
    ok = True
    for i in range(len(xs)-1):
        diff = abs(xs[i]-xs[i+1])
        if not 1<=diff<=3:
            ok = False
    return inc_or_dec and ok

lines = D.split('\n')
p1 = 0
p2 = 0
for line in lines:
    xs1 = list(map(int, line.split()))
    if is_good(xs1):
        p1 += 1

    good = False
    for j in range(len(xs1)):
        xs = xs1[:j] + xs1[j+1:]
        if is_good(xs):
            good = True
    if good:
        p2 += 1
print(p1)
print(p2)