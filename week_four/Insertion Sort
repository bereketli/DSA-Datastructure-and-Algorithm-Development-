#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'insertionSort1' function below.
#
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY arr
#

def insertionSort1(n, arr):
    for i in range(n):
        j = i - 1
        currentNum = arr[i]
        while j >= 0 and arr[j] > currentNum:
            arr[j + 1] = arr[j]
            j -= 1
            print(" ".join([str(num) for num in arr]))
        arr[j + 1] = currentNum
    print(" ".join([str(num) for num in arr]))
        
        

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)
