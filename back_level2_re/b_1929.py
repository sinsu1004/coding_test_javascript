from sys import stdin
input = stdin.readline

m, n = map(int, input().split())
lst = [0]*1000001
for num in range(2, n+1):
    lst[num] = num

for i in range(2, n+1):
    if lst[i] == 0:
        continue
    for j in range(i+i, n+1, i):
        lst[j] = 0

for result in range(m, n+1):
    if lst[result] == 0:
        continue
    print(lst[result])
