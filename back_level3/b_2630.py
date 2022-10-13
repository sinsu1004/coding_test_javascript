from sys import stdin


input=stdin.readline

n=int(input())
board=[list(map(int,input().split())) for _ in range(n)]
zero=0
one=0

def answer(x,y,n):
    global zero,one
    
    init=board[x][y]
    
    for i in range(x,n+x):
        for j in range(y,n+y):
            if board[i][j] != init:
                for k in range(2):
                    for l in range(2):
                        answer(x+k*n//2,y+l*n//2,n//2)
                        
                return
            
    if init == 0:
        zero +=1
    elif init ==1:
        one +=1
    return
answer(0,0,n)
print(zero)
print(one)
            