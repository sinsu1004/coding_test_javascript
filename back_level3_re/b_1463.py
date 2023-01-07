from sys import stdin
input = stdin.readline

dp = [0, 0]
n = int(input())

for i in range(2, n+1):
    num = dp[i-1]+1
    if i % 3 == 0:
        num = min(num, dp[i//3]+1)
    if i % 2 == 0:
        num = min(num, dp[i//2]+1)
    dp.append(num)
print(dp[-1])
