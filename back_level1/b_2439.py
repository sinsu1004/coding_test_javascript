data=int(input())
for i in range(data):
    for j in range(data):
        if(j>data-i-2):
            print("*",end="")
        else :
            print(" ",end="")
    
    print()