from sys import stdin
input = stdin.readline

answer = {}
n = int(input())
lst = list(map(int, input().split()))


ch_lst = set(lst)
ch_lst = sorted(list(ch_lst))

while ch_lst:
    q = ch_lst.pop()
    if q not in answer:
        answer[q] = len(ch_lst)
for i in lst:
    print(answer[i], end=" ")
