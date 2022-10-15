from collections import deque
from sys import stdin
input=stdin.readline

n,m=map(int,input().split())
lst=[[]for _ in range(n+1)]

freind = [0 for _ in range(n+1)]

def bfs(start,end):
    visited=[False for _ in range(n+1)]
    count=0
    que=deque([start])
    while True:
        dque=deque()
        for i in que:
            if visited[i] ==True:
                continue
            if end == i:
                return count
            visited[i] =True
            dque.extend(lst[i])
        que=dque
        count+=1
 
for i in range(m):
    a,b=map(int,input().split())
    lst[a].append(b)
    lst[b].append(a)
for i in range(1,n+1):
    sum=0
    for j in range(1,n+1):
        if i == j:
            continue
        sum+=bfs(i,j)
    freind[i]=sum
freind.pop(0)
print(freind.index(min(freind))+1)


    