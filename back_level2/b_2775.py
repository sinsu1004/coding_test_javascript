t=int(input())
for i in range(t):
    k=int(input())
    n=int(input())
    lst =[]
    for j in range(n):
        lst.append(j+1)
    for k in range(k):
        for i in range(n):
            if i ==0:
                 continue
            else:
                lst[i]+=lst[i-1]
    print(lst[-1])    
    