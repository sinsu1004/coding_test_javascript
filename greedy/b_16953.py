from sys import stdin
from collections import deque
input = stdin.readline


A, B = map(int, input().split())

q = deque()
q.append((A, 1))

while q:
    num, cnt = q.popleft()
    if num == B:
        print(cnt)
        break
    if num > B:
        continue

    q.append((num*10+1, cnt+1))
    q.append((num*2, cnt+1))
else:
    print(-1)
