from sys import stdin
input = stdin.readline

n = int(input())
lst = []
for _ in range(n):
    lst.append(int(input()))
lst.sort()
for value in lst:
    print(value)
