from collections import deque
from sys import stdin


input= stdin.readline

n,m=map(int,input().split())
lst=[[] for _ in range(n+1)]
visited=[False for _ in range(n+1)]
visited[0]=True
count=0

def dfs(start):
    global visited,lst,count
    if visited[start]:
        return
    
    num=deque([start])
    visited[start]=True
    while num:
        v= num.popleft()
        for i in lst[v]:
            if not visited[i]:
                num.append(i)
                visited[i]=True
    count+=1
    return
    

for i in range(m):
    u,v=map(int,input().split())
    lst[u].append(v)
    lst[v].append(u)

for i in range(1,n+1):
    dfs(i)
    if sum(visited) == len(visited):
        break
print(count)