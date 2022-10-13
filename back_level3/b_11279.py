
import heapq
from sys import stdin


input=stdin.readline

n=int(input())
heap=[]
for i in range(n):
    su = int(input())
    if su == 0:
        if len(heap) == 0 :
            print(0)
        else:
            print(heapq.heappop(heap)[1])
    else:
        heapq.heappush(heap,(-su,su))