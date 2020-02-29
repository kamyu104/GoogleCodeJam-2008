# Copyright (c) 2020 kamyu. All rights reserved.
#
# Google Code Jam 2008 Round 1B - Problem B. Number Sets
# https://code.google.com/codejam/contest/32017/dashboard#s=p1
#
# Time:  O(F * (B - A)), F is the max number of factors of integers in the interval [A, B]
#                      , F is at most 11 (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31) by the given limits
# Space: O(B - A)
#

from bisect import bisect_left, bisect_right
from itertools import islice

class UnionFind(object):
    def __init__(self, n):
        self.set = range(n)
        self.count = n

    def find_set(self, x):
        stk = []
        while self.set[x] != x:  # path compression.
            stk.append(x)
            x = self.set[x]
        while stk:
            self.set[stk.pop()] = x
        return x

    def union_set(self, x, y):
        x_root, y_root = map(self.find_set, (x, y))
        if x_root != y_root:
            self.set[min(x_root, y_root)] = max(x_root, y_root)
            self.count -= 1

# Template:
# https://github.com/kamyu104/GoogleCodeJam-2016/blob/master/World%20Finals/gallery-of-pillars.py
def sieve_of_eratosthenes(n):  # Time: O(M), Space: O(M)
    is_prime, primes = [True]*n, []
    for i in xrange(2, n):
        if not is_prime[i]:
            continue
        primes.append(i)
        for j in xrange(i+i, n, i):
            is_prime[j] = False
    return primes

def number_sets():
    A, B, P = map(int, raw_input().strip().split())
    union_find = UnionFind(B-A+1)
    start, end = bisect_left(PRIMES, P), bisect_right(PRIMES, B-A)
    for p in islice(PRIMES, start, end):
        left, right = ((A-1)//p+1)*p, B//p*p
        for i in xrange(left, right+1, p):
            union_find.union_set(left-A, i-A)
    return union_find.count

M = 10**6+1
PRIMES = sieve_of_eratosthenes(M)
for case in xrange(input()):
    print 'Case #%d: %s' % (case+1, number_sets())
