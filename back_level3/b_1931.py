from sys import stdin


input=stdin.readline


lst=[]
last=0
count=0
n=int(input())

for i in range(n):
    x,y=map(int,input().split())
    lst.append([x,y])

lst = sorted(lst,key=lambda x:x[0] )
lst = sorted(lst,key=lambda x:x[1] )

for i,j in lst:
    if i>=last:
        count+=1
        last=j

print(count)