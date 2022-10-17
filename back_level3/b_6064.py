
from sys import stdin


input=stdin.readline
def gi(m,n,x,y):
    while x<=m*n:
        if (x-y)%n ==0:
            return x
        x=x+m
    return -1

T=int(input())
for i in range(T):
    m,n,a,b=map(int,input().split())
    print(gi(m,n,a,b))
        
        
    