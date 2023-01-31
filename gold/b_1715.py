from sys import stdin
import heapq
input = stdin.readline

n = int(input())
heap = []
result = 0

for _ in range(n):
    heapq.heappush(heap, int(input()))
for _ in range(n-1):
    tmp = 0
    for _ in range(2):
        tmp += heapq.heappop(heap)
    heapq.heappush(heap, tmp)
    result += tmp
print(result)
