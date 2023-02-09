from sys import stdin
input = stdin.readline

n = int(input())
num = input().rstrip()
answer = 0
for i in num:
    answer += int(i)

print(answer)
