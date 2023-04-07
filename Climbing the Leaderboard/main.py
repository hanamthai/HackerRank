#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'climbingLeaderboard' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY ranked
#  2. INTEGER_ARRAY player
#

def Binary_Search(rank,score,left,right):
    if left >= right:
        if score < rank[left]:
            return left - 1
        else:
            return left
    else:
        mid = (left+right)//2
        if score == rank[mid]:
            return mid
        elif score < rank[mid]:
            return Binary_Search(rank,score,left,mid-1)
        else:
            return Binary_Search(rank,score,mid+1,right)

def climbingLeaderboard(ranked, player):
    # Write your code here
    score_of_rank = sorted(set(ranked))
    rank_of_player = []
    rank_of_player_tmp = []
    for i in player:
        tmp = Binary_Search(score_of_rank,i,0,len(score_of_rank)-1)
        rank_of_player_tmp.append(tmp)
    # format rank of player
    for i in rank_of_player_tmp:
        rank_of_player.append(len(score_of_rank)-i)
    return rank_of_player
        
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ranked_count = int(input().strip())

    ranked = list(map(int, input().rstrip().split()))

    player_count = int(input().strip())

    player = list(map(int, input().rstrip().split()))

    result = climbingLeaderboard(ranked, player)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
