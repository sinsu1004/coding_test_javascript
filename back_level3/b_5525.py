from sys import stdin

input=stdin.readline

n=int(input())
m=int(input())
lst=input().rstrip()
i=0
count =0
answer=0
while i<m-1:
    if lst[i:i+3] =="IOI":
        count+=1
        i+=2
        if count==n:
            answer+=1
            count-=1
    else:
        count=0
        i+=1
print(answer)