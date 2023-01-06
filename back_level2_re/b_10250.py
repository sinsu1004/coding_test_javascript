from sys import stdin
input = stdin.readline

n = int(input())
for _ in range(n):
    h, w, n = map(int, input().split())
    width = int(n/h)
    if n % h == 0:
        print(100*h+width)
    else:
        print(100*(n % h)+width+1)
