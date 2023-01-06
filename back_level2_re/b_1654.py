from sys import stdin
input = stdin.readline

k, n = map(int, input().split())
lst = []
for _ in range(k):
    lst.append(int(input()))


def calculation(num):
    global lst
    cnt = 0
    for index in lst:
        cnt += index // num
    return cnt


def binarySearch(value):
    global lst
    left = 1
    right = max(lst)
    while left <= right:
        mid = (left+right) // 2
        count = calculation(mid)
        if count >= value:
            left = mid + 1
        else:
            right = mid-1
    return right


print(binarySearch(n))
