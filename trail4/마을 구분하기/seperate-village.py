n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

visited=[[False for _ in range(n)] for _ in range(n)]

move=[(0, 1), (0, -1), (1, 0), (-1, 0)]

def dfs(st):
    q=[st]
    cnt=1
    while q:
        nowx, nowy=q.pop()
        visited[nowx][nowy]=True
        for dx, dy in move:
            tmpx, tmpy=nowx+dx, nowy+dy

            if 0<=tmpx<n and 0<=tmpy<n and not visited[tmpx][tmpy] and grid[tmpx][tmpy]==1:
                visited[tmpx][tmpy]=True
                q.append((tmpx, tmpy))
                cnt+=1
    return cnt

ans=0
ammount=[]

for i in range(n):
    for j in range(n):
        if not visited[i][j] and grid[i][j]:
            ammount.append(dfs((i, j)))
            ans+=1

ammount.sort()
print(ans)
for i in ammount:
    print(i)