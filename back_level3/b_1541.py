from sys import stdin


input=stdin.readline

lst = input().rstrip().split('-')
value=0
for i in lst[0].split('+'):
    value += int(i)
for i in lst[1:]:
    for j in i.split('+'):
        value -= int(j)

print(value)