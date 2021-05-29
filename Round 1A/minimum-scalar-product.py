# Copyright (c) 2018 kamyu. All rights reserved.
#
# Google Code Jam 2008 Round 1A - Problem A. Minimum Scalar Product
# https://code.google.com/codejam/contest/32016/dashboard
#
# Time:  O(NlogN)
# Space: O(1)
#

import operator
import itertools

def inner_product(vec1, vec2):
    return sum(itertools.imap(operator.mul, vec1, vec2))

def minimum_scalar_product():
    N = input()
    V1 = map(int, raw_input().strip().split())
    V2 = map(int, raw_input().strip().split())
    V1.sort()
    V2.sort(reverse=True)
    return inner_product(V1, V2)

for case in xrange(input()):
    print 'Case #%d: %s' % (case+1, minimum_scalar_product())
