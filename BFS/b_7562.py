from sys import stdin
from collections import deque
input = stdin.readline

T = int(input())

for _ in range(T):
    n = int(input())
    x, y = map(int, input().split())
    mx, my = map(int, input().split())

    board = [[0 for _ in range(n)] for _ in range(n)]
    visited = [[False for _ in range(n)] for _ in range(n)]

    q = deque()
    q.append((x, y))
    visited[x][y] = True

    tx = [1, 2, -1, -2, -2, -1, 1, 2]
    ty = [2, 1, 2, 1, -1, -2, -2, -1]

    while q:
        dx, dy = q.popleft()

        for i in range(8):
            px = dx + tx[i]
            py = dy + ty[i]

            if px == mx and py == my and not visited[px][py]:
                board[px][py] = board[dx][dy] + 1
                break
            elif 0 <= px < n and 0 <= py < n and not visited[px][py]:
                visited[px][py] = True
                board[px][py] = board[dx][dy] + 1
                q.append((px, py))
        else:
            continue
        break
    print(board[mx][my])
