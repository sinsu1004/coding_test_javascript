from sys import stdin

n=int(stdin.readline())
lst=[0] *10001

for i in range(n):
    num=int(stdin.readline())
    
    lst[num-1]=lst[num-1]+1
    
for i in range(10001):
    if lst[i] != 0:
        for j in range(lst[i]):
            print(i+1)
