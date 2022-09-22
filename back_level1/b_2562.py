data_list=[]
for i in range(9):
    a=int(input())
    data_list.append(a)
print(max(data_list))
print(data_list.index(max(data_list))+1)