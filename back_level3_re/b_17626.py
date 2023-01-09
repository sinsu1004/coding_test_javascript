import sys


def check(n):
    if (n**0.5).is_integer():
        return 1
    for i in range(1, int(n**0.5)+1):
        if (int(n-i*i)**0.5).is_integer():
            return 2
    for i in range(1, int(n**0.5)+1):
        for j in range(1, int((n-i*i)**0.5)+1):
            if ((n-i*i-j*j)**0.5).is_integer():
                return 3
    return 4


n = int(sys.stdin.readline())
print(check(n))
