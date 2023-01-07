from sys import stdin
from collections import deque

input = stdin.readline
n, m, v = map(int, input().split())
lst = [[] for i in range(n+1)]
visited = [False] * (n+1)
for _ in range(m):
    n1, n2 = map(int, input().split())
    lst[n1].append(n2)
    lst[n2].append(n1)


def dfs(graph, start_node, visited=[]):
    visited.append(start_node)
    print(start_node, end=" ")
    graph[start_node].sort()
    for node in graph[start_node]:
        if node not in visited:
            dfs(graph, node, visited)


def bfs(graph, start, visited):
    queue = deque([start])

    visited[start] = True

    while queue:
        num = queue.popleft()
        print(num, end=" ")

        for i in graph[num]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True


dfs(lst, v)
print()
bfs(lst, v, visited)
