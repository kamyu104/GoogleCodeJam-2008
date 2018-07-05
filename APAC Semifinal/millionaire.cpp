// Copyright (c) 2018 kamyu. All rights reserved.

/*
 * Google Code Jam 2008 APAC Semifinal - Problem C. Millionaire
 * https://codejam.withgoogle.com/codejam/contest/32005/dashboard#s=p2
 *
 * Time:  O(4^M)
 * Space: O(2^M)
 *
 */

#include <iostream>
#include <vector>

using std::cin;
using std::cout;
using std::endl;
using std::vector;
using std::max;
using std::min;

const int TARGET = 1000000;
const int MAX_X = 15;
double dp[2][(1 << MAX_X) + 1];

double millionaire() {
    uint64_t M, X;
    double P;
    cin >> M >> P >> X;
    dp[0][1] = 1.0;
    for (int m = 1; m <= M; ++m) {
        const auto n = 1 << m;
        auto& curRound = dp[m % 2];
        auto& nxtRound = dp[(m - 1) % 2];
        for (int sum = 0; sum <= n; ++sum) {
            curRound[sum] = nxtRound[sum / 2];
            const auto max_bet = min(sum, n - sum);
            for (int bet = 1; bet <= max_bet; ++bet) {
                const auto tmp = P * nxtRound[(sum + bet) / 2] +
                                 (1 - P) * nxtRound[(sum - bet) / 2];
                if (curRound[sum] < tmp) {
                    curRound[sum] = tmp;
                }
            }
        }
    }
    return dp[M % 2][X * (1 << M) / TARGET];
}

int main() {
    int T;
    cin >> T;
    for (int test = 1; test <= T; ++test) {
        cout << "Case #" << test << ": " << millionaire() << endl;
    }
    return 0;
}
