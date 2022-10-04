from sys import stdin

input=stdin.readline
t=int(input())
for i in range(t):
    dp=[0,1,1,1]
    n=int(input())
    if n>3:
        for i in range(4,n+1):
            dp.append(dp[i-2]+dp[i-3])
    print(dp[n])

