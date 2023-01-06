from sys import stdin
input = stdin.readline

n = int(input())
lst = []
for _ in range(n):
    lst.append(input().rstrip())
lst = set(lst)
lst = list(lst)

lst.sort()
lst.sort(key=len)
for result in lst:
    print(result)
