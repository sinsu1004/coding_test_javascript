from sys import stdin
input = stdin.readline

n = int(input())

lst = []
for _ in range(n):
    start, finish = map(int, input().split())
    lst.append([start, finish])
lst.sort(key=lambda x: x[0])
lst.sort(key=lambda x: x[1])

cnt = 0
last = 0
for i, j in lst:
    if i >= last:
        cnt += 1
        last = j

print(cnt)
