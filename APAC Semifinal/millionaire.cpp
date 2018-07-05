
// Copyright (c) 2018 kamyu. All rights reserved.

/*
 * Google Code Jam 2008 APAC Semifinal - Problem C. Millionaire
 * https://codejam.withgoogle.com/codejam/contest/32005/dashboard#s=p2
 *
 * Time:  O(M * 2^M)
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

const int MAX_X = 15;
double dp[2][(1 << MAX_X) + 1];

double millionaire() {
    static const int TARGET = 1000000;
    uint64_t M, X;
    double P;
    cin >> M >> P >> X;
    dp[0][1] = 1.0;
    for (int i = 1; i <= M; ++i) {
        const auto n = 1 << i;
        auto& curRound = dp[i % 2];
        auto& nxtRound = dp[(i - 1) % 2];
        for (int j = 0; j <= n; ++j) {
            curRound[j] = nxtRound[j / 2];
            const auto bet = min(j, n - j);
            for (int k = 0; k <= bet; ++k) {
                const auto tmp = P * nxtRound[(j + k) / 2] +
                                 (1 - P) * nxtRound[(j - k) / 2];
                if (curRound[j] < tmp) {
                    curRound[j] = tmp;
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
