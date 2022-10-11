t=int(input())
dx=[-1,1,0,0]
dy=[0,0,1,-1]

def bfs(x,y):
    queue = [(x,y)]
    matrix[x][y] = 0
    
    while queue:
        x,y = queue.pop(0)
        
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if nx<0 or ny>=height or nx>=width or ny<0:
                continue
            
            if matrix[nx][ny] == 1:
                queue.append((nx,ny))
                matrix[nx][ny] = 0



for i in range(t):
    width,height,num=map(int,input().split())
    matrix=[[0]*(height) for _ in range(width)]
    cnt=0
    
    for j in range(num):
        x,y=map(int,input().split())
        matrix[x][y]=1
    
    for a in range(width):
        for b in range(height):
            if matrix[a][b] ==1:
                bfs(a,b)
                cnt+=1
    print(cnt)
    