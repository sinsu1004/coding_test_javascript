# 1 2 3 4 5
# 1 2 4 7 13
# 11111 1112 1121 1211 2111 122 212 221 113 131 311 32 23
from sys import stdin
input = stdin.readline

dp = [1, 1, 2]
n = int(input())
for _ in range(n):
    num = int(input())
    if num <= len(dp)-1:
        print(dp[num])
    else:
        for i in range(len(dp), num+1):
            dp.append(dp[i-1]+dp[i-2]+dp[i-3])
        print(dp[num])
