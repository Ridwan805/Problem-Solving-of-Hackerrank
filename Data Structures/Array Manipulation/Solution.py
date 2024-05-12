#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'arrayManipulation' function below.      
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. 2D_INTEGER_ARRAY queries
#

def arrayManipulation(n, queries):
    # Initialize an array with zeros
    arr = [0] * n
    
    # Initialize a prefix sum array
    prefix_sum = [0] * (n + 1)
    
    # Process queries
    for start, end, val in queries:
        prefix_sum[start - 1] += val
        prefix_sum[end] -= val
    
    # Calculate the maximum sum
    max_sum = 0
    current_sum = 0
    for i in range(n):
        current_sum += prefix_sum[i]
        max_sum = max(max_sum, current_sum)
    
    return max_sum

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    queries = []

    for _ in range(m):
        queries.append(list(map(int, input().rstrip().split())))

    result = arrayManipulation(n, queries)

    fptr.write(str(result) + '\n')

    fptr.close()
