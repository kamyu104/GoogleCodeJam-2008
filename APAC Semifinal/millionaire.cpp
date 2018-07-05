
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

double millionaire() {
    static const int TARGET = 1000000;
    uint64_t M, X;
    double P;
    cin >> M >> P >> X;
    vector<vector<double>> dp(2, vector<double>((1 << M) + 1, 0.0));
    dp[0][1] = 1.0;
    for (int i = 1; i <= M; ++i) {
        for (int j = 0; j <= (1 << i); ++j) {
            dp[i % 2][j] = dp[(i - 1) % 2][j / 2];
            for (int k = 0; k <= min(j, (1 << i) - j); ++k) {
                dp[i % 2][j] = max(dp[i % 2][j],
                                   P * dp[(i - 1) % 2][(j + k) / 2] +
                                   (1 - P) * dp[(i - 1) % 2][(j - k) / 2]);
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
