from sys import stdin

input = stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    rank = []
    cnt = 1
    for _ in range(n):
        a, b = map(int, input().split())
        rank.append((a, b))
    rank.sort()
    tmp = rank[0][1]
    for i in range(1, n):
        if rank[i][1] < tmp:
            cnt += 1
            tmp = rank[i][1]
    print(cnt)
