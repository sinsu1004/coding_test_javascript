# - 을 발견하면 앞에 ( 치고
# - 를 발견하면 그앞에 )
# 발견못하면 마지막에 )
# 신박한거 split('-')나누면?? 55-50-40

from sys import stdin
input = stdin.readline


value = input().rstrip().split('-')
answer = 0
for num in value[0].split('+'):
    answer += int(num)
for minus in value[1:]:
    for i in minus.split('+'):
        answer -= int(i)
print(answer)
