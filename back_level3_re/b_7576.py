from sys import stdin
from collections import deque

input = stdin.readline

m, n = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
test = deque()
cnt = -1

for i in range(n):
    for j in range(m):
        if board[i][j] == 1:
            test.append([i, j])
while test:
    count = len(test)
    cnt += 1
    for _ in range(count):
        x, y = test.popleft()

        if x+1 < n:
            if board[x+1][y] == 0:
                board[x+1][y] = 1
                test.append([x+1, y])
        if x-1 >= 0:
            if board[x-1][y] == 0:
                board[x-1][y] = 1
                test.append([x-1, y])
        if y+1 < m:
            if board[x][y+1] == 0:
                board[x][y+1] = 1
                test.append([x, y+1])
        if y-1 >= 0:
            if board[x][y-1] == 0:
                board[x][y-1] = 1
                test.append([x, y-1])


def result(board):
    global cnt
    for i in range(n):
        if 0 in board[i]:
            return -1
    return cnt


print(result(board))
