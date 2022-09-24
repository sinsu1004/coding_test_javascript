n = int(input())
a =list(map(int,input().split()))
m =int(input())
m_a=list(map(int,input().split()))
a.sort()

for num in m_a:
    start,last=0,n-1
    isnum=False
    
    while start<=last:
        mid=(start+last)//2
        if num == a[mid]:
            isnum=True
            print(1)
            break
        elif num >a[mid]:
            start=mid+1
        elif num <a[mid]:
            last=mid-1
    if not isnum :
        print(0)