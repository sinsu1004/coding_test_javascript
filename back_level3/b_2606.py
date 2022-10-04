from collections import deque
from sys import stdin

input =stdin.readline

n=int(input())
m=int(input())
greph=[[] for i in range(n+1)]
visited=[0]*(n+1)
for i in range(m):
    a,b=map(int,input().split())
    greph[a]+=[b]
    greph[b]+=[a]

visited[1]=1
print(greph)


# def dfs(v):
#     visited[v]=1
#     for i in greph[v]:
#         if visited[i]==0:
#             dfs(i)
# dfs(1)
# print(sum(visited)-1)