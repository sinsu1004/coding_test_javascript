from sys import stdin
input = stdin.readline

n = int(input())
lst = []

for _ in range(n):
    userInput = int(input())
    if userInput == 0:
        lst.pop()
    else:
        lst.append(userInput)
print(sum(lst))
