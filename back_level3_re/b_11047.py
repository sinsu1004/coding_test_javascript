from sys import stdin
input = stdin.readline

n, k = map(int, input().split())
cnt = 0
lst = []
for _ in range(n):
    lst.append(int(input()))
for i in range(1, n+1):
    if k // lst[-i] != 0:
        cnt += k // lst[-i]
        k = k % lst[-i]
    if k == 0:
        break
print(cnt)
