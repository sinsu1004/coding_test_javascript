from collections import deque
from sys import stdin


input=stdin.readline

n,m,v=map(int,input().split())
lst=[[] for _ in range(n+1)]
visitd=[0 for _ in range(n+1)]

for i in range(m):
    a,b=map(int,input().split())
    lst[a].append(b)
    lst[b].append(a)

def bfs(start,que,visit):
    queue=deque()
    queue.append(start)
    visit[start]=1
    while queue:
        node=[]
        num= queue.popleft()
        print(num,end=" ")
        node.extend(que[num])
        for i in range(1,n+1):
            if visit[i] == 0 and i in node:
                queue.append(i)
                visit[i] =1
                
def dfs(graph,start,visited=[]):
    visited.append(start)
    print(start,end=" ")
    num=[]
    num.extend(graph[start])
    
    for i in range(1,n+1):
        if i not in visited and i in num:
            dfs(graph,i,visited)
   
       
dfs(lst,v)    
print()  
bfs(v,lst,visitd)