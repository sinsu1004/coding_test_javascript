# dp 1 2 3 4 5 6
from sys import stdin
input = stdin.readline

dp = [1, 1, 1, 1]
t = int(input())
for _ in range(t):
    n = int(input())
    if n < len(dp):
        print(dp[n])
        continue
    for i in range(len(dp), n+1):
        dp.append(dp[i-3]+dp[i-2])
    print(dp[n])
