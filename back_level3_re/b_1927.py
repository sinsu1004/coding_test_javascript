from sys import stdin
from collections import deque

input = stdin.readline


def bfs(startX, startY, type):
    visited[startX][startY] = True
    q = deque()
    q.append([startX, startY])
    if type:
        color = board[startX][startY]
    else:
        if board[startX][startY] == 'R' or board[startX][startY] == 'G':
            color = ['R', 'G']
        else:
            color = board[startX][startY]
    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < n:
                if board[nx][ny] in color and visited[nx][ny] == False:
                    q.append([nx, ny])
                    visited[nx][ny] = True


n = int(input())
board = [list(input().rstrip()) for _ in range(n)]
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

for k in range(2):
    cnt = 0
    visited = [[False for _ in range(n)] for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if visited[i][j] == True:
                continue
            if k == 0:
                bfs(i, j, True)
            elif k == 1:
                bfs(i, j, False)
            cnt += 1

    print(cnt, end=" ")
