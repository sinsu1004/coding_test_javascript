count =int(input())
point_list=list(map(int,input().split()))
max_p=max(point_list)

for i in range(len(point_list)):
    point_list[i]=point_list[i]/max_p*100
print(sum(point_list)/len(point_list))
