from sys import stdin
from collections import deque

input = stdin.readline

n, m = map(int, input().split())
board = [list(input().rstrip()) for _ in range(n)]


def bfs():
    global board
    visited = [[0]*m for _ in range(n)]
    queue = deque()
    queue.append([0, 0])
    visited[0][0] = 1
    while queue:
        x, y = queue.popleft()
        if x+1 < n:
            if visited[x+1][y] == 0 and board[x+1][y] == '1':
                visited[x+1][y] = visited[x][y] + 1
                queue.append([x+1, y])
        if x-1 >= 0:
            if visited[x-1][y] == 0 and board[x-1][y] == '1':
                visited[x-1][y] = visited[x][y] + 1
                queue.append([x-1, y])
        if y+1 < m:
            if visited[x][y+1] == 0 and board[x][y+1] == '1':
                visited[x][y+1] = visited[x][y] + 1
                queue.append([x, y+1])
        if y-1 >= 0:
            if visited[x][y-1] == 0 and board[x][y-1] == '1':
                visited[x][y-1] = visited[x][y] + 1
                queue.append([x, y-1])
    return visited[-1][-1]


print(bfs())
