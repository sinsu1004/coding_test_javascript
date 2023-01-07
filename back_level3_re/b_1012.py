from sys import stdin
from collections import deque

input = stdin.readline

t = int(input())


def bfs(graph, userX, userY, n, m):
    queue = deque()
    queue.append([userX, userY])
    graph[userX][userY] = 0
    while queue:
        x, y = queue.popleft()
        if x+1 < n:
            if graph[x+1][y] == 1:
                graph[x+1][y] = 0
                queue.append([x+1][y])
        if x-1 >= 0:
            if graph[x-1][y] == 1:
                graph[x-1][y] = 0
                queue.append([x-1][y])
        if y+1 < m:
            if graph[x][y+1] == 1:
                graph[x][y+1] = 0
                queue.append([x][y+1])
        if y-1 >= 0:
            if graph[x][y-1] == 1:
                graph[x][y-1] = 0
                queue.append([x][y-1])
    return graph


for _ in range(t):
    m, n, k = map(int, input().split())
    board = [[0 for _ in range(n)] for _ in range(m)]
    for _ in range(k):
        x, y = map(int, input().split())
        board[x][y] = 1
    cnt = 0
    for i in range(m):
        for j in range(n):
            if board[i][j] == 1:
                cnt += 1
                queue = deque()
                queue.append([i, j])
                board[i][j] = 0
                while queue:
                    x, y = queue.popleft()
                    if x+1 < m:
                        if board[x+1][y] == 1:
                            board[x+1][y] = 0
                            queue.append([x+1, y])
                    if x-1 >= 0:
                        if board[x-1][y] == 1:
                            board[x-1][y] = 0
                            queue.append([x-1, y])
                    if y+1 < n:
                        if board[x][y+1] == 1:
                            board[x][y+1] = 0
                            queue.append([x, y+1])
                    if y-1 >= 0:
                        if board[x][y-1] == 1:
                            board[x][y-1] = 0
                            queue.append([x, y-1])
    print(cnt)
