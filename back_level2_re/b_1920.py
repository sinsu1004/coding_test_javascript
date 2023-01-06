from sys import stdin
input = stdin.readline

n = int(input())
lst_a = list(map(int, input().split()))
lst_a.sort()
m = int(input())
lst = list(map(int, input().split()))


def binarySearch(n, list):
    left = 0
    right = len(list)-1
    while left <= right:
        bot = int((left + right)//2)
        if list[bot] == n:
            return 1
        elif list[bot] < n:
            left = bot+1
        elif list[bot] > n:
            right = bot - 1
    return 0


for i in lst:
    print(binarySearch(i, lst_a))
