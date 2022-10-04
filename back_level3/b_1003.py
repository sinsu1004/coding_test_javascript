from sys import stdin



t=int(stdin.readline())
for i in range(t):
    n=int(stdin.readline())
    lst_zero=[1,0]
    lst_one=[0,1]
  
    for i in range(2,n+1):
        lst_zero.append(lst_zero[i-1]+lst_zero[i-2])
        lst_one.append(lst_one[i-1]+lst_one[i-2])
    print("%d %d" %(lst_zero[n],lst_one[n]))
            