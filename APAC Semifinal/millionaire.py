# Copyright (c) 2018 kamyu. All rights reserved.
#
# Google Code Jam 2008 APAC Semifinal - Problem C. Millionaire
# https://codejam.withgoogle.com/codejam/contest/32005/dashboard#s=p2
#
# Time:  O(4^M)
# Space: O(2^M)
#

TARGET = 1000000
MAX_M = 15
dp = [[0.0 for _ in xrange(2**MAX_M+1)] for _ in xrange(2)]

def millionaire():
    M, P, X = raw_input().strip().split()
    M, P, X = int(M), float(P), int(X)
    dp[0][1] = 1.0
    for m in xrange(1, M+1):
        n = 2**m
        curRound, nxtRound = dp[m%2], dp[(m-1)%2]
        for sum in xrange(n+1):
            max_bet = min(sum, n-sum)
            curRound[sum] = nxtRound[sum//2];
            for bet in xrange(1, max_bet+1):
                curRound[sum] = max(curRound[sum],
                                    P*nxtRound[(sum+bet)//2] + (1.0-P)*nxtRound[(sum-bet)//2])
    return dp[M%2][X*(2**M)//TARGET]

for case in xrange(input()):
    print 'Case #%d: %s' % (case+1, millionaire())


