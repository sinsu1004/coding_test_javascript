from sys import stdin
input = stdin.readline

n = int(input())
dp = [0]
lst = [int(input()) for _ in range(n)]

if n < 3:
    if n == 1:
        print(lst[0])
    elif n == 2:
        print(lst[0]+lst[1])
else:

    dp.append(lst[0])
    dp.append(lst[0]+lst[1])
    for i in range(3, n+1):
        dp.append(max((dp[i-2]+lst[i-1]), (dp[i-3]+lst[i-2]+lst[i-1])))
    print(dp[-1])
