from sys import stdin


n=int(stdin.readline())
n_data=list(map(int,stdin.readline().split()))
m=int(stdin.readline())
m_data=list(map(int,stdin.readline().split()))
data=[0]*m
for i in range(m):
    for j in range(n):
        if n_data[j] == m_data[i]:
            data[i]+=1

for a in data:
    print(a,end=" ")

