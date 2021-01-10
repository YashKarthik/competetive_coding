import math
import os
import random
import re
import sys


def equalStacks(h1, h2, h3):

    while sum(h1) != sum(h2) and sum(h2) != sum(h3):
        h1.pop(0) if h1 else None
        h2.pop(0) if h2 else None
        h3.pop(0) if h3 else None

    if sum(h1) == sum(h2) and sum(h2) == sum(h3):
        return sum(h1)

    else:
        return 0


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    h1 = list(map(int, input().rstrip().split()))

    h2 = list(map(int, input().rstrip().split()))

    h3 = list(map(int, input().rstrip().split()))

    result = equalStacks(h1, h2, h3)

    fptr.write(str(result) + '\n')

    fptr.close()
