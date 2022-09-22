data =list(map(int,input().split()))
sum=0
for i in range(len(data)):
    sum+=data[i]**2
print(sum%10)