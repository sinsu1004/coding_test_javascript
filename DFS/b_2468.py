import copy
from sys import stdin
import sys
sys.setrecursionlimit(100000)

input = stdin.readline


def dfs(tmp, x, y, index):
    global n
    tmp[x][y] = index
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    for i in range(4):
        tx = x + dx[i]
        ty = y + dy[i]
        if 0 <= tx < n and 0 <= ty < n and tmp[tx][ty] > index:
            dfs(tmp, tx, ty, index)


n = int(input())
result = [0]
board = [list(map(int, input().split())) for _ in range(n)]
maxNum = 0

for i in board:
    maxNum = max(maxNum, max(i))

for i in range(maxNum):
    tmp = copy.deepcopy(board)
    cnt = 0
    for x in range(n):
        for y in range(n):
            if tmp[x][y] > i:
                dfs(tmp, x, y, i)
                cnt += 1
    result.append(cnt)

print(max(result))
