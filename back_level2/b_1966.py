test_n=int(input())

for i in range(test_n):
    n,m =map(int,input().split())
    que=list(map(int,input().split()))
    idx=list(range(len(que)))
    idx[m]="target"
    cnt=0
    while True:
        if que[0] == max(que):
            cnt +=1
            
            if idx[0] == "target":
                print(cnt)
                break
            else:
                que.pop(0)
                idx.pop(0)
        else :
            que.append(que.pop(0))
            idx.append(idx.pop(0))
    
                