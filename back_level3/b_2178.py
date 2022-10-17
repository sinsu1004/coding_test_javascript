from collections import deque
from sys import stdin
input=stdin.readline

def dfs(x,y):
    q=deque()
    q.append((x,y))
    visited[x][y]=1
    while q:
        v,w=q.popleft()
        
        if v+1<n and int(miro[v+1][w]) ==1 and visited[v+1][w]==0:
            visited[v+1][w]=visited[v][w]+1
            q.append((v+1,w))
            
        if w+1<m and int(miro[v][w+1]) ==1 and visited[v][w+1]==0:
            visited[v][w+1]=visited[v][w]+1
            q.append((v,w+1))
            
        if v-1>=0 and int(miro[v-1][w]) ==1 and visited[v-1][w]==0:
            visited[v-1][w]=visited[v][w]+1
            q.append((v-1,w))
           
    return


n,m=map(int,input().split())
miro=[list(input().rstrip()) for _ in range(n)]
visited=[[0 for _ in range(m)] for _ in range(n)]
dfs(0,0)
print(visited[n-1][m-1])


