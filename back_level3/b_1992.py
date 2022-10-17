from collections import deque
from sys import stdin


input=stdin.readline

def anwer(x,y,n):
    global q
    init =lst[x][y]
    
    for i in range(x,n+x):
        for j in range(y,n+y):
            if init != lst[i][j]:
                q+="("
                for k in range(2):
                    for l in range(2):
                        anwer(x+k*n//2,y+l*n//2,n//2)
                q+=")"
                return
    if int(init) ==0:
        q+="0"
    else:
        q+="1"
    return



n=int(input())
lst =[list(input().rstrip()) for _ in range(n)]
q=""
anwer(0,0,n)
print(q)