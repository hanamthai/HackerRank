#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'formingMagicSquare' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY s as parameter.
#

def formingMagicSquare(s):
    # Write your code here
    # There are 8 ways to make a 3 x 3 magic square.
    # So we just need to subtract 2 matrices and get the smallest value.
    magic_square = [[8, 1, 6, 3, 5, 7, 4, 9, 2], [6, 1, 8, 7, 5, 3, 2, 9, 4], [4, 3, 8, 9, 5, 1, 2, 7, 6], [2, 7, 6, 9, 5, 1, 4, 3, 8],  [2, 9, 4, 7, 5, 3, 6, 1, 8], [4, 9, 2, 3, 5, 7, 8, 1, 6], [6, 7, 2, 1, 5, 9, 8, 3, 4], [8, 3, 4, 1, 5, 9, 6, 7, 2]]
    
    # convert from 2 dimensional matrix to 1 dimensional matrix
    s_1_dimensional = []
    for i in s:
        s_1_dimensional += i
    
    min_cost = 99999
    index_magic_square = 99999
    for i in range(len(magic_square)):
        cost = 0
        for j in range(len(s_1_dimensional)):
            cost += abs(s_1_dimensional[j] - magic_square[i][j])
        if cost < min_cost:
            min_cost = cost
    return min_cost
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = []

    for _ in range(3):
        s.append(list(map(int, input().rstrip().split())))

    result = formingMagicSquare(s)

    fptr.write(str(result) + '\n')

    fptr.close()
