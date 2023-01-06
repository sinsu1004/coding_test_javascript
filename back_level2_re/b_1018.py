from sys import stdin
input = stdin.readline

x, y = map(int, input().split())
lst = []
result = []

for _ in range(x):
    lst.append(list(input().rstrip()))


def bf(x, y):
    draw1 = 0
    draw2 = 0
    for i in range(x, x+8):
        for j in range(y, y+8):
            if (i+j) % 2 == 0:
                if lst[i][j] == 'W':
                    draw1 += 1
                elif lst[i][j] == 'B':
                    draw2 += 1
            else:
                if lst[i][j] == 'B':
                    draw1 += 1
                elif lst[i][j] == 'W':
                    draw2 += 1
    return min(draw1, draw2)


for i in range(0, x-7):
    for j in range(0, y-7):
        result.append(bf(i, j))
print(min(result))
