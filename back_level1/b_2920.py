data=list(map(int,input().split()))
data_sort=sorted(data)
data_revers=list(reversed(data_sort))
if data == data_sort:
    print("ascending")
elif data == data_revers:
    print("descending")
else :
    print("mixed")