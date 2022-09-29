from sys import stdin

n,m=map(int,stdin.readline().split())
a=set()
b=set()
for i in range(n):
    num=stdin.readline().rstrip()
    a.add(num)
for i in range(m):
    num=stdin.readline().rstrip()
    b.add(num)
    
result=sorted(a&b)
print(len(result))
for i in result:
    print(i)