from sys import stdin

n=int(stdin.readline())
lst=[]
dp=[]
for i in range(n):
    lst.append(int(stdin.readline()))
if n<3:
    if n==1:
        print(lst[0])
    elif n==2:
        print(lst[0]+lst[1])
    else:
        print(max(lst[0]+lst[2],lst[1]+lst[2]))
else:       
    dp.append(lst[0])
    dp.append(lst[0]+lst[1])
    dp.append(max(lst[0]+lst[2],lst[1]+lst[2]))
    for i in range(3,n):
        dp.append(max(lst[i]+dp[i-2],lst[i]+lst[i-1]+dp[i-3]))

    print(dp.pop())