import sys
from collections import deque
sys.setrecursionlimit(10000)

input = sys.stdin.readline

n, m = map(int, input().split())
visited = []
lst = [[] for _ in range(n+1)]
cnt = 0


def dfs(start):
    visited.append(start)
    for node in lst[start]:
        if node not in visited:
            dfs(node)


for _ in range(m):
    start, finish = map(int, input().split())
    lst[start].append(finish)
    lst[finish].append(start)

for i in range(1, n+1):
    if i not in visited:
        dfs(i)
        cnt += 1
    if len(visited) == n:
        break
print(cnt)
