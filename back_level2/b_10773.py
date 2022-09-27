n=int(input())
lst=[]
for i in range(n):
    value=int(input())
    if value ==0:
        lst.pop()
    else :
        lst.append(value)

print(sum(lst))