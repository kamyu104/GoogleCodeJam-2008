# [GoogleCodeJam 2008](https://codingcompetitions.withgoogle.com/codejam/archive/2008) ![Language](https://img.shields.io/badge/language-Python-orange.svg) [![License](https://img.shields.io/badge/license-MIT-blue.svg)](./LICENSE) ![Progress](https://img.shields.io/badge/progress-5%20%2F%2037-ff69b4.svg)

Python solutions of Google Code Jam 2008. Solution begins with `*` means it will get TLE in the largest data set (total computation amount > `10^8`, which is not friendly for Python to solve in 5 ~ 15 seconds). A `4-minute` timer is set for the small dataset and a `8-minute` timer is set for the large dataset this year.

* [Qualification Round](https://github.com/kamyu104/GoogleCodeJam-2008#qualification-round)
* [Round 1A](https://github.com/kamyu104/GoogleCodeJam-2008#round-1a)
* [Round 1B](https://github.com/kamyu104/GoogleCodeJam-2008#round-1b)
* [Round 1C](https://github.com/kamyu104/GoogleCodeJam-2008#round-1c)
* [Round 2](https://github.com/kamyu104/GoogleCodeJam-2008#round-2)
* [Round 3](https://github.com/kamyu104/GoogleCodeJam-2008#round-3)
* [APAC Semifinal](https://github.com/kamyu104/GoogleCodeJam-2008#apac-semifinal)
* [AMER Semifinal](https://github.com/kamyu104/GoogleCodeJam-2008#amer-semifinal)
* [EMEA Semifinal](https://github.com/kamyu104/GoogleCodeJam-2008#emea-semifinal)
* [World Finals](https://github.com/kamyu104/GoogleCodeJam-2008#world-finals)
* [Code Jam 2009](https://github.com/kamyu104/GoogleCodeJam-2009)

## Qualification Round
| # | Title | Solution | Time | Space | Difficulty | Tag | Note |
|---| ----- | -------- | ---- | ----- | ---------- | --- | ---- |
|A| [Saving the Universe](https://code.google.com/codejam/contest/32013/dashboard#s=p0)| | | | | | |
|B| [Train Timetable](https://code.google.com/codejam/contest/32013/dashboard#s=p1)| | | | | | |
|C| [Fly Swatter](https://code.google.com/codejam/contest/32013/dashboard#s=p2)| | | | | | |

## Round 1A
| # | Title | Solution | Time | Space | Difficulty | Tag | Note |
|---| ----- | -------- | ---- | ----- | ---------- | --- | ---- |
|A| [Minimum Scalar Product](https://code.google.com/codejam/contest/32016/dashboard#s=p0)| [Python](./Round%201A/minimum-scalar-product.py)| _O(NlogN)_ | _O(NlogN)_ | Easy | | Sort |
|B| [Milkshakes](https://code.google.com/codejam/contest/32016/dashboard#s=p1)| | | | | | |
|C| [Numbers](https://code.google.com/codejam/contest/32016/dashboard#s=p2)| [Python](./Round%201A/numbers.py) | _O(logN)_ | _O(1)_ | Easy | | Matrix Exponentiation |

## Round 1B
| # | Title | Solution | Time | Space | Difficulty | Tag | Note |
|---| ----- | -------- | ---- | ----- | ---------- | --- | ---- |
|A| [Crop Triangles](https://code.google.com/codejam/contest/32017/dashboard#s=p0)| | | | | | |
|B| [Number Sets](https://code.google.com/codejam/contest/32017/dashboard#s=p1)| [Python](./Round%201B/number_sets.py) | _O(F * (B - A))_ | _O(B - A)_ | Easy | | Prime Sieving, Binary Search, Union Find |
|C| [Mousetrap](https://code.google.com/codejam/contest/32017/dashboard#s=p2)| | | | | | |

## Round 1C
| # | Title | Solution | Time | Space | Difficulty | Tag | Note |
|---| ----- | -------- | ---- | ----- | ---------- | --- | ---- |
|A| [Text Messaging Outrage](https://code.google.com/codejam/contest/32015/dashboard#s=p0)| | | | | | |
|B| [Ugly Numbers](https://code.google.com/codejam/contest/32015/dashboard#s=p1)| | | | | | |
|C| [Increasing Speed Limits](https://code.google.com/codejam/contest/32015/dashboard#s=p2)| | | | | | |

## Round 2
| # | Title | Solution | Time | Space | Difficulty | Tag | Note |
|---| ----- | -------- | ---- | ----- | ---------- | --- | ---- |
|A| [Cheating a Boolean Tree](https://code.google.com/codejam/contest/32001/dashboard#s=p0)| | | | | | |
|B| [Triangle Areas](https://code.google.com/codejam/contest/32001/dashboard#s=p1)| | | | | | |
|C| [Star Wars](https://code.google.com/codejam/contest/32001/dashboard#s=p2)| | | | | | |
|D| [PermRLE](https://code.google.com/codejam/contest/32001/dashboard#s=p3)| | | | | | |

## Round 3
| # | Title | Solution | Time | Space | Difficulty | Tag | Note |
|---| ----- | -------- | ---- | ----- | ---------- | --- | ---- |
|A| [How Big Are the Pockets?](https://code.google.com/codejam/contest/32002/dashboard#s=p0)| | | | | | |
|B| [Portal](https://code.google.com/codejam/contest/32002/dashboard#s=p1)| | | | | | |
|C| [No Cheating](https://code.google.com/codejam/contest/32002/dashboard#s=p2)| [Python](./Round%203/no_cheating.py) | _O(M * N * sqrt(M * N)_ | _O(M * N)_ | Easy | | Bipartite Matching |
|D| [Endless Knight](https://code.google.com/codejam/contest/32002/dashboard#s=p2)| | | | | | |

## APAC Semifinal
| # | Title | Solution | Time | Space | Difficulty | Tag | Note |
|---| ----- | -------- | ---- | ----- | ---------- | --- | ---- |
|A| [What are Birds?](https://code.google.com/codejam/contest/32005/dashboard#s=p0)| | | | | | |
|B| [Apocalypse Soon](https://code.google.com/codejam/contest/32005/dashboard#s=p1)| | | | | | |
|C| [Millionaire](https://codejam.withgoogle.com/codejam/contest/32005/dashboard#s=p2)| [C++](./APAC%20Semifinal/millionaire.cpp) [PyPy](./APAC%20Semifinal/millionaire.py)| _O(4^M)_ | _O(2^M)_ | Medium | | DP |
|D| [Modern Art Plagiarism](https://code.google.com/codejam/contest/32005/dashboard#s=p2)| | | | | | |

## AMER Semifinal
| # | Title | Solution | Time | Space | Difficulty | Tag | Note |
|---| ----- | -------- | ---- | ----- | ---------- | --- | ---- |
|A| [Mixing Bowls](https://code.google.com/codejam/contest/32008/dashboard#s=p0)| | | | | | |
|B| [Code Sequence](https://code.google.com/codejam/contest/32008/dashboard#s=p1)| | | | | | |
|C| [Test Passing Probability](https://code.google.com/codejam/contest/32008/dashboard#s=p2)| | | | | | |
|D| [King](https://code.google.com/codejam/contest/32008/dashboard#s=p3)| | _O(R * C * 2^C)_ | _O(R * C * 2^C)_ | Very Hard | | DP, Brute Force |

## EMEA Semifinal
| # | Title | Solution | Time | Space | Difficulty | Tag | Note |
|---| ----- | -------- | ---- | ----- | ---------- | --- | ---- |
|A| [Scaled Triangle](https://code.google.com/codejam/contest/32010/dashboard#s=p0)| | | | | | |
|B| [Painting a Fence](https://code.google.com/codejam/contest/32010/dashboard#s=p1)| | | | | | |
|C| [Rainbow Trees](https://code.google.com/codejam/contest/32010/dashboard#s=p2)| | | | | | |
|D| [Bus Stops](https://code.google.com/codejam/contest/32010/dashboard#s=p3)| | | | | | |

## World Finals

| # | Title | Solution | Time | Space | Difficulty | Tag | Note |
|---| ----- | -------- | ---- | ----- | ---------- | --- | ---- |
|A| [Juice](https://code.google.com/codejam/contest/32011/dashboard#s=p0)| | | | | | |
|B| [Ping Pong Balls](https://code.google.com/codejam/contest/32011/dashboard#s=p1)| | | | | | |
|C| [Mine Layer](https://code.google.com/codejam/contest/32011/dashboard#s=p2)| | | | | | |
|D| [Bridge Builders](https://code.google.com/codejam/contest/32011/dashboard#s=p3)| | | | | | |
|E| [The Year of Code Jam](https://code.google.com/codejam/contest/32011/dashboard#s=p4)| | | | | | |
