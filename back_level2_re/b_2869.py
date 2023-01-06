from sys import stdin
input = stdin.readline

a, b, v = map(int, input().split())


def test(a, b, v):
    num = (v-b)/(a-b)
    if num == int(num):
        return int(num)
    return int(num)+1


print(test(a, b, v))
