from sys import stdin



n=int(stdin.readline())
lst=list(map(int,stdin.readline().split()))
lst.sort()
for i in range(1,len(lst)):
    lst[i]=lst[i]+lst[i-1]
print(sum(lst))

