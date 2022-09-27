n,m=map(int,input().split())
lst=list(map(int,input().split()))
start=1
last=max(lst)
while start<=last:
    mid=(start+last)//2
    sum=0
    for i in lst:
        if i>=mid:
            sum+=i-mid
    if sum >=m:
        start=mid+1
    else :
        last=mid-1
    
print(last)
        
            
    