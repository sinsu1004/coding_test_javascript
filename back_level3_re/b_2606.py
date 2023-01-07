from sys import stdin
from collections import deque

input = stdin.readline

n = int(input())
lst = [[] for _ in range(n+1)]
cnt = 0

m = int(input())
for _ in range(m):
    n1, n2 = map(int, input().split())
    lst[n1].append(n2)
    lst[n2].append(n1)


def dfs(graph, v, visited=[]):
    global cnt
    visited.append(v)
    for i in graph[v]:
        if i not in visited:
            cnt += 1
            dfs(graph, i, visited)


dfs(lst, 1)
print(cnt)
