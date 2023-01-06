from sys import stdin
input = stdin.readline

n = int(input())
lst = []
stack = []


def bf(n):
    global lst, stack
    cnt = 0
    answer = True
    for _ in range(n):
        num = int(input())

        while cnt < num:
            cnt += 1
            stack.append(cnt)
            lst.append("+")
        if stack[-1] == num:
            stack.pop()
            lst.append("-")
        else:
            answer = False
    return answer


if bf(n):
    for result in lst:
        print(result)
else:
    print("NO")
