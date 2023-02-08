from sys import stdin
from collections import deque
input = stdin.readline


def bfs(x, y, board):
    q = deque()
    q.append((x, y))
    board[x][y] = 0
    dx = [1, -1, 0, 0, 1, -1, 1, -1]
    dy = [0, 0, 1, -1, 1, -1, -1, 1]

    while q:
        x, y = q.popleft()
        for i in range(8):
            tx = x + dx[i]
            ty = y + dy[i]
            if 0 <= tx < len(board) and 0 <= ty < len(board[0]) and board[tx][ty] == 1:
                q.append((tx, ty))
                board[tx][ty] = 0

    return 1


while True:
    w, h = map(int, input().split())
    if not w and not h:
        break
    board = [list(map(int, input().split())) for _ in range(h)]
    answer = 0
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 1:
                answer += bfs(i, j, board)
    print(answer)
