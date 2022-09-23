
num =int(input())
sosu=list(map(int,input().split()))
cnt=0

for i in sosu:
    enum=True
    if i >1:
        for j in range(2,i):
            if i % j ==0:
                enum=False
        if enum == True:
            cnt +=1

print(cnt)
