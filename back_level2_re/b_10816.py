# 이분탐색 찾고 -> count -> 중복제거
from sys import stdin
input = stdin.readline

n = int(input())
n_lst = list(map(int, input().split()))
n_lst.sort()
result = {}
for num in n_lst:
    if num in result:
        result[num] += 1
    else:
        result[num] = 1

m = int(input())
m_lst = list(map(int, input().split()))
for num in m_lst:
    if num not in result:
        print(0, end=' ')
    else:
        print(result[num], end=' ')
