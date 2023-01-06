from sys import stdin
input = stdin.readline

n = int(input())
lst = []

for _ in range(n):
    lst.append(list(map(int, input().split())))
lst.sort(key=lambda x: x[1])
lst.sort(key=lambda x: x[0])

for result in lst:
    print(result[0], result[1])
