from sys import stdin
from heapq import heappop, heappush
input = stdin.readline


t = int(input())

for count in range(t):
    n = int(input())
    max_heap = []
    min_heap = []
    visited = [False for _ in range(n)]

    for k in range(n):
        value, num = input().rstrip().split()
        num = int(num)
        if value == "I":
            heappush(min_heap, (num, k))
            heappush(max_heap, (-num, k))
            visited[k] = True
        elif value == "D":
            if num == 1:
                while max_heap and not visited[max_heap[0][1]]:
                    heappop(max_heap)
                if max_heap:
                    visited[max_heap[0][1]] = False
                    heappop(max_heap)
            elif num == -1:
                while min_heap and not visited[min_heap[0][1]]:
                    heappop(min_heap)
                if min_heap:
                    visited[min_heap[0][1]] = False
                    heappop(min_heap)
    while max_heap and not visited[max_heap[0][1]]:
        heappop(max_heap)
    while min_heap and not visited[min_heap[0][1]]:
        heappop(min_heap)

    if not max_heap:
        print('EMPTY')
    else:
        print(f"{-max_heap[0][0]} {min_heap[0][0]}")
