
while True:
    num =input()
    if num == '.':
        break
    else:
        stack=[]
        for i in num:
            if i == '(':
                stack.append(i)
            elif i == '[':
                stack.append(i)
            elif i == ')':
                if stack and stack[-1] == '(':
                    stack.pop()
                else:
                    print('no')
                    break
            elif i == ']':
                if stack and stack[-1] == '[':
                    stack.pop()
                else:
                    print('no')
                    break
                
        else :
            if stack:
                print("no")
            else:
                print("yes")
                    