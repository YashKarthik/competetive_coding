"""
Hackerrank problem: https://www.hackerrank.com/challenges/equal-stacks/problem
"""

import math
import os
import random
import re
import sys


def equalStacks(h1, h2, h3):

    h_1 = [sum(h1[index:]) for index in range(len(h1))]
    h_2 = [sum(h2[index:]) for index in range(len(h2))]
    h_3 = [sum(h3[index:]) for index in range(len(h3))]

    len_dict = {
        len(h_1): h_1,
        len(h_2): h_2,
        len(h_3): h_3,
    }

    min_stack = len_dict[min(len_dict.keys())]
    iters = len(min_stack)
    for elem in min_stack:
        iters -= 1
        if elem in h_1 and elem in h_2 and elem in h_3:
            return elem
        elif iters == 0:
            return 0


if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')
    first_multiple_input = input().rstrip().split()
    h1 = list(map(int, input().rstrip().split()))
    h2 = list(map(int, input().rstrip().split()))
    h3 = list(map(int, input().rstrip().split()))
    result = equalStacks(h1, h2, h3)
    print(result)
    #fptr.write(str(result) + '\n')
    # fptr.close()
