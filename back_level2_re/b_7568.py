from sys import stdin
input = stdin.readline

n = int(input())
lst = []
result = []

for _ in range(n):
    lst.append(list(map(int, input().split())))

for i in range(n):
    cnt = 1
    for j in range(n):
        if i == j:
            continue
        if lst[i][0] < lst[j][0] and lst[i][1] < lst[j][1]:
            cnt += 1
    result.append(cnt)

for rank in result:
    print(rank, end=" ")
