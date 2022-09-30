from sys import stdin



n,m=map(int,stdin.readline().split())
lst={}
for i in range(n):
    address,password=stdin.readline().split()
    lst[address]=password
for j in range(m):
    address=stdin.readline().rstrip()
    print(lst[address])