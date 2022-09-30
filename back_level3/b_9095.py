from sys import stdin


n=int(stdin.readline().rstrip())


for i in range(n):
    dp=[0,1,2,4]
    num=int(stdin.readline().rstrip())
    for j in range(4,num+1):
        dp.append(dp[j-1]+dp[j-2]+dp[j-3])
    print(dp[num])