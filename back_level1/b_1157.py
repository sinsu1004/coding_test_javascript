data=input().upper()
data_set=list(set(data))
data_list=[]

for i in data_set:
    cnt=data.count(i)
    data_list.append(cnt)
    
if data_list.count(max(data_list)) > 1 :
    print('?')
else:
    data_in=data_list.index(max(data_list))
    print(data_set[data_in])