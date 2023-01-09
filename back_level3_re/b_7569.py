from sys import stdin
from collections import deque

input = stdin.readline


def bfs():
    global cnt

    while start:
        cnt += 1
        point = len(start)
        for _ in range(point):
            x, y, z = start.popleft()
            for i in range(6):
                dx = x + fx[i]
                dy = y + fy[i]
                dz = z + fz[i]

                if 0 <= dx < h and 0 <= dy < n and 0 <= dz < m:
                    if tomato[dx][dy][dz] == 0:
                        tomato[dx][dy][dz] = 1
                        start.append([dx, dy, dz])


def result():
    global cnt
    for i in tomato:
        for j in i:
            if 0 in j:
                return -1
    return cnt


m, n, h = map(int, input().split())
tomato = [[list(map(int, input().split())) for _ in range(n)]
          for _ in range(h)]
start = deque()
fx = [1, -1, 0, 0, 0, 0]
fy = [0, 0, 1, -1, 0, 0]
fz = [0, 0, 0, 0, 1, -1]
cnt = -1
answer = True

for i in range(h):
    for j in range(n):
        for k in range(m):
            if tomato[i][j][k] == 1:
                start.append([i, j, k])
bfs()
print(result())
