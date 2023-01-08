from sys import stdin
from collections import deque
input = stdin.readline


def bfs(start):
    global k, max
    visited = [0 for _ in range(max+1)]
    queue = deque()
    queue.append(start)
    while queue:
        num = queue.popleft()
        if num == k:
            return visited[num]
        for i in (num-1, num+1, num*2):
            if 0 <= i <= max and visited[i] == 0:
                visited[i] = visited[num]+1
                queue.append(i)


n, k = map(int, input().split())
max = 100000
print(bfs(n))
