#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countingValleys' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER steps
#  2. STRING path
#

def countingValleys(steps, path):
    count_down =0
    count_valley =0
    for one_step in path: 
        if one_step == "D":
            count_down -=1
        if count_down ==-1 and one_step == "U":
            count_valley +=1
        if one_step == "U":
            
            count_down +=1
      
    return count_valley
    
    # Write your code here

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    steps = int(input().strip())

    path = input()

    result = countingValleys(steps, path)

    fptr.write(str(result) + '\n')

    fptr.close()
