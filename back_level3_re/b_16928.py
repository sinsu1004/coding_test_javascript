from sys import stdin
from collections import deque
input = stdin.readline


def bfs(start):
    visited = [False for _ in range(100+1)]
    cnt = 0
    q = deque()
    q.append(start)
    visited[start] = True

    while q:
        cnt += 1
        count = len(q)
        for _ in range(count):
            num = q.popleft()
            for i in range(1, 7):
                if num+i == 100:
                    return cnt
                elif num+i in move and visited[move[num+i]] == False:
                    visited[move[num+i]] = True
                    q.append(move[num+i])
                elif num+i not in move and visited[num+i] == False:
                    visited[num+i] = True
                    q.append(num+i)


n, m = map(int, input().split())
move = {}
for _ in range(n+m):
    point, move_point = map(int, input().split())
    move[point] = move_point

print(bfs(1))
