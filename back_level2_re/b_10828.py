from collections import deque
from sys import stdin
input = stdin.readline

n = int(input())
result = deque()
for _ in range(n):
    lst = input().split()
    if lst[0] == 'push':
        result.append(lst[1])
    elif lst[0] == 'pop':
        if len(result) == 0:
            print(-1)
        else:
            print(result.pop())
    elif lst[0] == 'size':
        print(len(result))
    elif lst[0] == 'empty':
        if len(result) == 0:
            print(1)
        else:
            print(0)
    elif lst[0] == 'top':
        if len(result) == 0:
            print(-1)
        else:
            print(result[-1])
