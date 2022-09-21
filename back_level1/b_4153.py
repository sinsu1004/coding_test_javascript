while True:
    data=list(map(int,input().split()))
    max_data=max(data)
    if sum(data) == 0:
        break
    data.remove(max_data)
    if data[0] ** 2  + data[1] ** 2 == max_data ** 2 :
        print("right")
    else:
        print("wrong")