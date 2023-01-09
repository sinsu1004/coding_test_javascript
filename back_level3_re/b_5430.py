from sys import stdin
from collections import deque
input = stdin.readline

t = int(input())

for _ in range(t):
    p = input().rstrip()
    n = int(input())
    lst = deque(input().rstrip()[1:-1].split(","))
    if n == 0:
        lst = deque()
    error = False
    answer = ""
    cnt = 0
    for i in p:
        if i == 'R':
            cnt += 1
        elif i == 'D':
            if len(lst) == 0:
                error = True
                break
            if cnt % 2 == 0:
                lst.popleft()
            else:
                lst.pop()

    if not error:
        if cnt % 2 != 0:
            lst.reverse()
        print("["+",".join(lst)+"]")
        continue
    print('error')
