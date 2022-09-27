n=int(input())
lst=[]
stack=[]
answer=[]
cnt=1
enum=True
for i in range(n):
    num = int(input())
    while cnt<=num:
        stack.append(cnt)
        answer.append('+')
        cnt+=1
    if stack[-1] == num:
        answer.append('-')
        stack.pop()
    else:
        enum=False
if enum==False:
    print('NO')
else:
    for i in answer:
        print(i)
        
