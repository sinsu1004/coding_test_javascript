a,b,v=map(int,input().split())

if a>=v:
    print(1)
else:
    if a-b > v-a:
        print(2)
    else:
        if (v-a)%(a-b)==0:
            print((v-a)//(a-b)+1)
        else:
            print((v-a)//(a-b)+2)

