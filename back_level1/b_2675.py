count=int(input())

for i in range(count):
    a,b=input().split()
    c=""
    b=list(b)
    for j in b:
        for k in range(int(a)):
            c+=j
            
    print(c)