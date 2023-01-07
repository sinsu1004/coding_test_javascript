from sys import stdin
input = stdin.readline

n = int(input())
lst = sorted(list(map(int, input().split())))

for i in range(1, n):
    lst[i] = lst[i]+lst[i-1]
print(sum(lst))

# 1 2 3 3 4
# 1 3 6 9 13
