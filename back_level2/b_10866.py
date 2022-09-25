from sys import stdin

n=int(stdin.readline())
lst=[]
for i in range(n):
    num=stdin.readline().split()
    if num[0] == "push_front":
        lst.append(num[1])
    elif num[0] == "push_back":
        lst.insert(0,num[1])
    elif num[0] == "pop_front":
        if len(lst) ==0:
            print(-1)
        else:
            print(lst.pop())
    elif num[0] == "pop_back" :
        if len(lst) ==0:
            print(-1)
        else:
            print(lst.pop(0))
    elif num[0] == "size" :
        print(len(lst))
    elif num[0] == "empty":
        if len(lst) ==0:
            print(1)
        else:
            print(0)
    elif num[0] == "front":
        if len(lst) ==0:
            print(-1)
        else:
            print(lst[len(lst)-1])
    elif num[0] == "back":
        if len(lst) ==0:
            print(-1)
        else:
            print(lst[0])
            
        