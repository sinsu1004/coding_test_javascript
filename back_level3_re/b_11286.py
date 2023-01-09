from sys import stdin
from heapq import heappush, heappop
input = stdin.readline

heap = []
n = int(input())
for _ in range(n):
    num = int(input())
    if num == 0:
        if len(heap) == 0:
            print(0)
            continue
        print(heappop(heap)[1])
        continue
    heappush(heap, (abs(num), num))
