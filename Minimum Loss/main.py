#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'minimumLoss' function below.
#
# The function is expected to return an INTEGER.
# The function accepts LONG_INTEGER_ARRAY price as parameter.
#

def minimumLoss(price):
    # Write your code here
    price_sort = sorted(price,reverse = True)
    result = price_sort[0] # result
    for i in range(len(price_sort)-1):
        tmp = price_sort[i] - price_sort[i+1]
        if tmp < result and price.index(price_sort[i]) < price.index(price_sort[i+1]):
            result = tmp
    return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    price = list(map(int, input().rstrip().split()))

    result = minimumLoss(price)

    fptr.write(str(result) + '\n')

    fptr.close()
