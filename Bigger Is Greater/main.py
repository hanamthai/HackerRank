#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'biggerIsGreater' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING w as parameter.
#

def biggerIsGreater(w):
    # Write your code here
    l = [*w]
    if l == sorted(l, reverse=True):
        return 'no answer'
                
    for j in range(1, len(l)):
        for i in range(j):
            #Find which character to swap.
            if l[-i-1] > l[-j-1]:
                #Swap characters.
                l[-i-1], l[-j-1] = l[-j-1], l[-i-1]
                #Sort characters that follow swapped character.
                l = l[:-j] + sorted(l[-j:])
                return ''.join(l)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    T = int(input().strip())

    for T_itr in range(T):
        w = input()

        result = biggerIsGreater(w)

        fptr.write(result + '\n')

    fptr.close()
