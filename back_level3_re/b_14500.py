from sys import stdin


input = stdin.readline

n, r, c = map(int, input().rstrip().split())

vist = 0
while n != 0:
    n -= 1
    size = 2**n

    if r < size and c < size:
        vist += 0

    elif r < size and c >= size:
        vist += size*size
        c -= size
    elif r >= size and c < size:
        vist += size*size*2
        r -= size
    else:
        vist += size*size*3
        r -= size
        c -= size
print(vist)
