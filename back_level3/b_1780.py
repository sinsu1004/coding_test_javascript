from sys import stdin


input= stdin.readline
n = int(input().rstrip())
board=[list(map(int,input().split())) for _ in range(n)]
plus=0
minus=0
zero=0

def answer(x,y,n):
    global plus,minus,zero
    init=board[x][y]
    
    for i in range(x,x+n):
        for j in range(y,y+n):
            if board[i][j] != init:
                for k in range(3):
                    for l in range(3):
                        answer(x+k*n//3,y+l*n//3,n//3)
                
                return
    
    if init == 0:
        zero+=1
    elif init == 1:
        plus+=1
    elif init == -1:
        minus+=1
    return
answer(0,0,n)
print(minus)
print(zero)
print(plus)
        