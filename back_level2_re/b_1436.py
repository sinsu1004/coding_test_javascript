from sys import stdin
input = stdin.readline

n = int(input())
cnt = 1
start = 666
while n != cnt:
    start += 1
    if "666" in str(start):
        cnt += 1
print(start)
