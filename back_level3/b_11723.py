from sys import stdin


s=set()
n=int(stdin.readline().rstrip())

for i in range(n):
    num=stdin.readline().split()
    if num[0]=='add':
        if int(num[1]) not in s:
            s.add(int(num[1]))
    elif num[0] == 'remove':
        if int(num[1]) in s:
            s.remove(int(num[1]))
    elif num[0] == 'check':
        if int(num[1]) in s:
            print(1)
        else:
            print(0)
    elif num[0] == 'toggle':
        if int(num[1]) in s:
            s.remove(int(num[1]))
        else:
            s.add(int(num[1]))
    elif num[0] == 'all':
        s.update([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20])
    elif num[0] == 'empty':
        s.clear()