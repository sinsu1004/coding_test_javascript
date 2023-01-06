from sys import stdin
input = stdin.readline

n, m = map(int, input().split())
lst = list(map(int, input().split()))
max = 0


def sum(i, j, k):
    return lst[i]+lst[j]+lst[k]


for i in range(0, n-2):
    for j in range(i+1, n-1):
        for k in range(j+1, n):
            value = sum(i, j, k)
            if value <= m and value > max:
                max = value
print(max)
