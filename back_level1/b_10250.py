t=int(input())
for i in range(t) :
    h,w,n=map(int,input().split())
    if n%h == 0 :
        answer=int(n/h + h*100)
    else:
        answer=int(n/h + n%h*100+1)
    print(answer)
    
    