n,m,b=map(int,input().split())
arr=[]
target=[]
for i in range(n):
    lst=list(map(int,input().split()))
    target.append(max(lst,key=lst.count))
    arr.append(lst)
print(arr)




