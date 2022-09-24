from sys import stdin

n=int(stdin.readline())
l=list(stdin.readline())

sum=0

for i in range(n):
    sum +=(ord(l[i])-96)*(31**i)
print(sum%1234567891)
