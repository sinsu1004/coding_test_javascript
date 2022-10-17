from collections import deque
from sys import stdin

input=stdin.readline
n=int(input())
board=[list(map(int,(input().rstrip()))) for _ in range(n)]
num=[]
xl=[1,-1,0,0]
yl=[0,0,1,-1]
for i in range(n):
    for j in range(n):
        if board[i][j] == 1 :
            q=deque()
            q.append((i,j))
            board[i][j]=board[i][j]+1
            count=1
            while q:
                x,y=q.popleft()
                for k in range(4):
                    dx=x+xl[k]
                    dy=y+yl[k]
                    if dx<0 or dx>=n or dy<0 or dy>=n:
                        continue
                    elif board[dx][dy] == 1 :
                        q.append((dx,dy))
                        board[dx][dy]=board[x][y]+1
                        count+=1
            num.append(count)

print(len(num))
num.sort()
for i in num:
    print(i)
         
                    
                    
                
            
