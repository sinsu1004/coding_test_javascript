from sys import stdin


n=int(stdin.readline())
que=[]
for i in range(n):
    num=stdin.readline().split()
    if num[0] == "push":
        que.insert(0,num[1])
    elif num[0] == "pop":
        if len(que)==0:
            print(-1)
        else :
            print(que.pop())
            
    elif num[0] == "size":
        print(len(que))
    elif num[0] == "empty":
        if len(que)==0:
            print(1)
        else:
            print(0)
    elif num[0] == "front":
        if len(que)==0:
            print(-1)
        else :
            print(que[len(que)-1])
    elif num[0] == "back":
        if len(que)==0:
            print(-1)
        else :
            print(que[0])
    
    
        
    