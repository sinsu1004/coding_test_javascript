data1,data2 =map(int,input().split())
ren=list()
for i in range(data1):
    ren.append(int(input()))

start=1
end =max(ren)

while(start<=end) :
    mid = (start+end)//2
    count=0
    for i in ren:
        count+=i//mid
    if count >= data2:
        start=mid+1
    else:
        end=mid-1
    
print(end)
        
