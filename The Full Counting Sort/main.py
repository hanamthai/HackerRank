#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countSort' function below.
#
# The function accepts 2D_STRING_ARRAY arr as parameter.
#

def countSort(arr):
    # Write your code here
    # the number of element in the array_res is max(arr[:,0]) + 1
    length_arr_res = 0
    for i in arr:
        if int(i[0]) > int(length_arr_res):
            length_arr_res = int(i[0])
    arr_res = [[] for i in range(length_arr_res+1)]
    # find first half array and convert it to '-'.
    for i in range(len(arr)//2):
        arr_res[int(arr[i][0])].append('-')
    # add last half array
    for i in range(len(arr)//2,len(arr)):
        arr_res[int(arr[i][0])].append(arr[i][1])
    # print it out
    for i in arr_res:
        for j in i:
            print(j,end=' ')
        
    

if __name__ == '__main__':
    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(input().rstrip().split())

    countSort(arr)
