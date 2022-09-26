from sys import stdin

n=int(stdin.readline())
n_list=sorted(list(map(int,stdin.readline().split())))
m=int(stdin.readline())
m_list=list(map(int,stdin.readline().split()))

cnt={}

for i in n_list:
    if i in cnt:
        cnt[i]+=1
    else:
        cnt[i]=1

for i in m_list:
    if i in cnt:
        print(cnt[i],end=' ')
    else:
        print(0,end=' ')