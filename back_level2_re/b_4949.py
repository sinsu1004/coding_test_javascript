from sys import stdin
input = stdin.readline


def test(userInput):
    stack = []
    for index in userInput:
        if index == "(" or index == "[":
            stack.append(index)
        elif (index == ")" or index == "]") and len(stack) == 0:
            return False
        elif (index == ")" and "(" != stack[-1]) or (index == "]" and "[" != stack[-1]):
            return False
        elif (index == ")" and "(" == stack[-1]) or (index == "]" and "[" == stack[-1]):
            stack.pop()
    if len(stack) + len(stack) == 0:
        return True
    return False


while True:
    userInput = input().rstrip()
    if userInput == '.':
        break
    if test(userInput):
        print("yes")
    else:
        print("no")
