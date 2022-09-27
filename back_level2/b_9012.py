from sys import stdin



n=int(stdin.readline())

for i in range(n):
    lst=list(input())
    stack =[]
    for j in lst:
        if j == '(':
            stack.append(j)
        elif j == ')':
            if len(stack) != 0 :
                stack.pop()
            else:
                print("NO")
                break
    else:
        if not stack:
            print("YES")
        else:
            print("NO")