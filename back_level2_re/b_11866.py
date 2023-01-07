from sys import stdin
input = stdin.readline

n, k = map(int, input().split())
circle = [i for i in range(1, n+1)]

print("<", end="")
while len(circle) != 1:
    for _ in range(k-1):
        circle.append(circle.pop(0))
    print(circle.pop(0), end=", ")
print(circle.pop(), end="")
print(">")

# 1 2 3 4 5 6 7
# 0 1 2 3 4 5 6
