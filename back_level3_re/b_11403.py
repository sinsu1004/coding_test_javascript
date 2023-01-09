from sys import stdin
from collections import deque
input = stdin.readline


def bfs(start, finish):
    visited = [False for _ in range(n)]
    q = deque()
    visited[start] = True
    q.append(start)
    while q:
        data = q.popleft()
        for i in lst[data]:
            if i == finish:
                return True
            if not visited[i]:
                visited[data] = True
                q.append(i)
    return False


n = int(input())
lst = [[] for _ in range(n)]

for i in range(n):
    num = list(map(int, input().rstrip().split()))
    for j in range(n):
        if num[j] == 1:
            lst[i].append(j)

for i in range(n):
    for j in range(n):
        if bfs(i, j):
            print(1, end=" ")
            continue
        print(0, end=" ")

    print()
