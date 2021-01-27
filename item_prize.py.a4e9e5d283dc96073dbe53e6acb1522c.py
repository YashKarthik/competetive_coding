"""
Hackerrank challenge: https://www.hackerrank.com/challenges/py-collections-ordereddict/problem?isFullScreen=false
"""

from collections import OrderedDict
bill = OrderedDict()
N = int(input())

for item in range(N):
    inputt = input().split()
    if ' '.join(inputt[:-1]) not in bill.keys():
        bill[' '.join(inputt[:-1])] = int(inputt[-1])

    else:
        bill[' '.join(inputt[:-1])] += int(inputt[-1])


for item, prize in bill.items():
    print(item, prize)
