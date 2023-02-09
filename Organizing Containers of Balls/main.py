#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'organizingContainers' function below.
#
# The function is expected to return a STRING.
# The function accepts 2D_INTEGER_ARRAY container as parameter.
#

def organizingContainers(container):
    # Write your code here
    # total a column
    total_col = []
    for i in range(len(container[0])):
        sum_col = 0
        for j in range(len(container)):
            sum_col += container[j][i]
        total_col.append(sum_col)
    
    # total a row
    total_row = []
    for i in container:
        total_row.append(sum(i))
    
    # sort total row and column
    total_col.sort()
    total_row.sort()
        
    for i in range(len(total_col)):
        if total_col[i] != total_row[i]:
            return "Impossible"
    return "Possible"
        
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        n = int(input().strip())

        container = []

        for _ in range(n):
            container.append(list(map(int, input().rstrip().split())))

        result = organizingContainers(container)

        fptr.write(result + '\n')

    fptr.close()
