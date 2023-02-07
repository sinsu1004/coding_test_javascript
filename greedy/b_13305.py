from sys import stdin
input = stdin.readline

n = int(input())
street = list(map(int, input().split()))
lst = list(map(int, input().split()))
answer = 0
min_cost = lst[0]

for i in range(n-1):
    if min_cost > lst[i]:
        answer += lst[i] * street[i]
        min_cost = lst[i]
        continue
    answer += street[i] * min_cost

print(answer)
