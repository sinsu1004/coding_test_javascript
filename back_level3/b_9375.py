from sys import stdin


input=stdin.readline

t=int(input())

for i in range(t):
    n=int(input())
    lst={}
    for i in range(n):
        value,key=input().split()
        if lst.get(key) ==None:
            lst[key]=1
        else:
            lst[key]+=1
    cnt=1
    for i in lst.values():
        cnt*=i+1
    print(cnt-1)
        