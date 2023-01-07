from sys import stdin
from collections import deque

input = stdin.readline

n = int(input())
board = [list(input().rstrip()) for _ in range(n)]
visited = [[False] * n for _ in range(n)]
result = []


def bfs(a, b):
    global visited, board
    cnt = 1
    visited[a][b] = True
    queue = deque()
    queue.append([a, b])
    while queue:
        x, y = queue.popleft()
        if x+1 < n:
            if board[x+1][y] == '1' and visited[x+1][y] == False:
                visited[x+1][y] = True
                cnt += 1
                queue.append([x+1, y])
        if x-1 >= 0:
            if board[x-1][y] == '1' and visited[x-1][y] == False:
                visited[x-1][y] = True
                cnt += 1
                queue.append([x-1, y])
        if y+1 < n:
            if board[x][y+1] == '1' and visited[x][y+1] == False:
                visited[x][y+1] = True
                cnt += 1
                queue.append([x, y+1])
        if y-1 >= 0:
            if board[x][y-1] == '1' and visited[x][y-1] == False:
                visited[x][y-1] = True
                cnt += 1
                queue.append([x, y-1])

    return cnt


for x in range(n):
    for y in range(n):
        if board[x][y] == '1' and visited[x][y] == False:
            result.append(bfs(x, y))
result.sort()
print(len(result))
for answer in result:
    print(answer)
