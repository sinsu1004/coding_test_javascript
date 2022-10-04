from sys import stdin

input=stdin.readline
n,m=map(int,input().split())
lst=list(map(int,input().split()))
dp=[0]
dp.append(lst[0])
for i in range(2,n+1):
    dp.append(dp[i-1]+lst[i-1])
for i in range(m):
    start,last=map(int,input().split())
    
    print(dp[last]-dp[start-1])