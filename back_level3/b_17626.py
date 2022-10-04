n=int(input())
dp=[0,1]

for i in range(2,n+1):
    min_v=4
    start=1
    while (start**2)<=i:
        min_v=min(min_v,dp[i-(start**2)])
        start+=1
    dp.append(min_v+1)
print(dp[n])