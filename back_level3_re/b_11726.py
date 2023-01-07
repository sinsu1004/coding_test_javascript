# 1 2 3 4 5
# 1 2 3 5 8
from sys import stdin
input = stdin.readline

dp = [1, 1]
n = int(input())
for i in range(2, n+1):
    dp.append(dp[i-2]+dp[i-1])
print(dp[-1] % 10007)
