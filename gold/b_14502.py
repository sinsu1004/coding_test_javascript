from sys import stdin
from collections import deque
from itertools import combinations
import copy


input = stdin.readline

one, two = map(int, input().split())

board = [list(map(int, input().split())) for _ in range(one)]
visited = [[0 for _ in range(two)] for _ in range(one)]
start = []
zero_lst = []
result = []


def bfs(op):
    global start, board, visited, one, two
    Board = copy.deepcopy(board)
    Visited = copy.deepcopy(visited)
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    cnt = 0
    q = deque()
    for tmp in start:
        q.append(tmp)
        Visited[tmp[0]][tmp[1]] = 1

    for tmp in op:
        x, y = tmp
        Board[x][y] = 1

    while q:
        x, y = q.popleft()
        for i in range(4):
            tx = dx[i] + x
            ty = dy[i] + y
            if 0 <= tx < one and 0 <= ty < two and not Visited[tx][ty]:
                if Board[tx][ty] == 0:
                    q.append((tx, ty))
                    Visited[tx][ty] = 1
                    Board[tx][ty] = 2

    for index in Board:
        cnt += index.count(0)

    return cnt


for i in range(one):
    for j in range(two):
        if board[i][j] == 2:
            start.append((i, j))
        elif board[i][j] == 0:
            zero_lst.append((i, j))

tmp = list(combinations(zero_lst, 3))


for num in tmp:
    result.append(bfs(num))

print(max(result))
