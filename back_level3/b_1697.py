from collections import deque
from sys import stdin

def dfs():
    q=deque()
    q.append(n)
    
    while q:
        v=q.popleft()
        if v == k:
            print(lst[v])
            break
        for i in (v-1,v+1,v*2):
            if 0<=i<=max and lst[i] ==0:
                lst[i]=lst[v]+1
                q.append(i)

max=100000
input=stdin.readline
n,k=map(int,input().split())
lst=[0 for _ in range(max+1)]
dfs()