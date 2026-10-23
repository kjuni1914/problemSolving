from collections import deque

n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

move=[(0, 1), (1, 0)]


visited=[[False for _ in range(m)] for _ in range(n)]
if grid[0][0]:
    dq=deque([(0, 0)])
else:
    dq=[]
visited[0][0]=True
ans=0

while dq:
    nowx, nowy=dq.pop()
    if nowx==n-1 and nowy==m-1:
        ans=1

    for dx, dy in move:
        tmpx, tmpy=nowx+dx, nowy+dy
        if 0<=tmpx<n and 0<=tmpy<m and not visited[tmpx][tmpy] and grid[tmpx][tmpy]:
            visited[tmpx][tmpy]=True
            dq.append((tmpx, tmpy))

print(ans)