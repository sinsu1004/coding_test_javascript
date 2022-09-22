count = int(input())

for i in range(count):
    data=list(input())
    point=0
    point_sum=0
    for j in range(len(data)):
        if data[j] == "O":
            point+=1
        else:
            point=0
        point_sum+=point
    print(point_sum)
    