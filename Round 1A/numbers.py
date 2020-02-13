# Copyright (c) 2020 kamyu. All rights reserved.
#
# Google Code Jam 2008 Round 1A - Problem C. Numbers
# https://code.google.com/codejam/contest/32016/dashboard#s=p2
#
# Time:  O(logN)
# Space: O(1)
#

from itertools import izip

def matrix_mult(A, B):
    ZB = zip(*B)
    return [[sum(a*b for a, b in izip(row, col)) % MOD \
                for col in ZB] for row in A]

def matrix_expo(A, K):
    result = [[int(i==j) for j in xrange(len(A))] \
                for i in xrange(len(A))]
    while K:
        if K % 2:
            result = matrix_mult(result, A)
        A = matrix_mult(A, A)
        K //= 2
    return result

def numbers():
    return "%03d" % ((2*matrix_expo(A, input())[0][0]-1)%MOD)

A = [[3, 5], [1, 3]]
MOD = 1000
for case in xrange(input()):
    print 'Case #%d: %s' % (case+1, numbers())
