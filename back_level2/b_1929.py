start,last = map(int,input().split())

for i in range(start,last+1):
    if i !=1:
        rst=False
        for j in range(2,int(i**0.5)+1):
            if i % j ==0:
                rst=True
                break
        if rst ==False:
            print(i)
        