#!/bin/python3

import math
import os
import random
import re
import sys
import math

#
# Complete the 'encryption' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def encryption(s):
    # Write your code here
    L = math.sqrt(len(s))
    col = math.ceil(L)
    row = math.floor(L)
    lst_encryption = []
    index = 0
    for i in range(col):
        sub_encryption = [s[index]]
        index_tmp = index
        while 1:
            if index_tmp + col < len(s):
                index_tmp += col
                sub_encryption.append(s[index_tmp])
            else:
                lst_encryption.append(sub_encryption)
                break
        index += 1
    encryption_str = ""
    for i in lst_encryption:
        for j in i:
            encryption_str += j
        encryption_str += " "
    return encryption_str
        
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = encryption(s)

    fptr.write(result + '\n')

    fptr.close()
