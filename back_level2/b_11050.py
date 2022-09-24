from sys import stdin
def fac(n):
    if(n>1):
        return n*fac(n-1)
    else:
        return 1


n,k =map(int,stdin.readline().split())
print(fac(n)//(fac(n-k)*fac(k)))
