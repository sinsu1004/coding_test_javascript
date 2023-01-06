from collections import deque

n = int(input())

for _ in range(n):
    nums = input()
    stack = deque()
    for num in nums:
        if num == ")" and len(stack) == 0:
            stack.append("(")
            break
        if num == ")" and len(stack) != 0:
            stack.pop()
        if num == "(":
            stack.append("(")
    if len(stack) == 0:
        print("YES")
    else:
        print("NO")
