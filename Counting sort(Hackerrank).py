#!/bin/python3

import math
import os
import random
import re
import sys

import os

def countingSort(arr):
    freq_array = [0] * 100  # Frequency array with 100 elements initialized to zeros

    # Count occurrences of each element in the input array
    for num in arr:
        freq_array[num] += 1

    return freq_array

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = countingSort(arr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()

