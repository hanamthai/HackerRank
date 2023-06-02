#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'substrings' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING n as parameter.
#
"""
example: 12384

1 => 1 = 1
12 => 1 + (2 + 12) = 15
123 => 1 + 2 + 12 + (3 + 23 + 123) = 164
1238 => 1 + 2 + 12 + 3 + 23 + 123 + (8 + 38 + 238 + 1238) = 1.686
12384 => 1 + 2 + 12 + 3 + 23 + 123 + 8 + 38 + 238 + 1238 + (4 + 84 + 384 + 2384 + 12384) = 16.926

f(1) =>    1 = 1 = 1
f(2) =>    12 = f(1) + (2 + 12) = 15
f(3) =>    123 = f(2) + (3 + 23 + 123) = 164
f(4) =>    1238 = f(3) + (8 + 38 + 238 + 1238) = 1.686
f(5) =>    12384 = f(4) + (4 + 84 + 384 + 2384 + 12384) = 16.926

Let's say:
df(2) = (2 + 12)
df(3) = (3 + 23 + 123)
and so on...

So the formula would be:
f(2) = f(1) + df(2)
f(3) = f(2) + df(3)
and so on...


We know that a number (ex: 675) can be refactored into
600 + 70 + 5 = 675
So in case of df(3): (3) + (23) + (123) can be refactored into
= (3) + (20 + 3) + (100 + 20 + 3)
= 1 * 100 + 2 * 20 + 3 * 3

Now, we try to refactor all of these:
df(2) => (2 + 12) = 1 * 10 + 2 * 2
df(3) => (3 + 23 + 123) = 1 * 100 + 2 * 20    + 3 * 3
df(4) => (8 + 38 + 238 + 1238) = 1 * 1000  + 2 * 200 + 3 * 30    + 4 * 8
df(5) => (4 + 84 + 384 + 2384 + 12384) = 1 * 10000 + 2 * 2000    + 3 * 300    + 4 * 80 + 5 * 4

Take a look at df(5) and df(4):
1 * 10000 + 2 * 2000 + 3 * 300 + 4 * 80 + 5 * 4 = 10 * (1 * 1000 + 2 * 200 + 3 * 30    + 4 * 8) + 5 * 4
df(5) = 10 * df(4) + 5 * 4

There for we can generalize the formula:
df(n) = 10 * df(n-1) + n * digits[n]
f(n) = f(n-1) + df(n)
"""

def substrings(n):
    mod = 10**9 + 7
    digits = list(map(int, n))
    N = len(n)

    fn = digits[0]
    dfn = fn

    for i in range(1, N):
        current_digit = digits[i]

        dfn = (10 * dfn + (i + 1) * current_digit) % mod
        fn = (fn + dfn) % mod

    return fn

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = input()

    result = substrings(n)

    fptr.write(str(result) + '\n')

    fptr.close()
