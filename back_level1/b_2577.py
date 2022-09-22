a=int(input())
b=int(input())
c=int(input())
data_x=a*b*c
data=list(str(data_x))


for i in range(10):
    print(data.count(str(i)))
    