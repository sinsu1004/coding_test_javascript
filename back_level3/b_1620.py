from sys import stdin

n,m=map(int,stdin.readline().split())
lst={}
for i in range(n):
    num=stdin.readline().rstrip()
    lst[i+1]=num
    lst[num]=i+1
for i in range(m):
    num=stdin.readline().rstrip()
    if num.isdigit():
        print(lst[int(num)])
    else:
        print(lst[num])