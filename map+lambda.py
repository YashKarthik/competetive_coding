# https://www.hackerrank.com/challenges/map-and-lambda-expression/problem#

N = int(input())
fibbs = [0, 1]
for i in range(2, N):
    fibbs.append(fibbs[i-1] + fibbs[i-2])

print(list(map(lambda x: x ** 3, fibbs)))
