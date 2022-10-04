from sys import stdin


n,k=map(int,stdin.readline().split())
lst=[]
for i in range(n):
    lst.append(int(stdin.readline().rstrip()))
start=0
last=len(lst)-1
count=0
while start<=last:
    mid=(start+last)//2
    if lst[mid] <= k:
        start=mid+1
    else:
        last=mid-1
while k!=0:
    if k//lst[last] ==0:
        last-=1
    else:
        count+=k//lst[last]
        k= k%lst[last]
print(count)