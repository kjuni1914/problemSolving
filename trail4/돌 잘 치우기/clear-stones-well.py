import copy

n, k, m = map(int, input().split())

grid = [list(map(int, input().split())) for _ in range(n)]

r = []
c = []
for _ in range(k):
    ri, ci = map(int, input().split())
    r.append(ri - 1)
    c.append(ci - 1)

rocks=[]

for x in range(n):
    for y in range(n):
        if grid[x][y]==1:
            rocks.append((x, y))

visited=[[False for _ in range(n)] for _ in range(n)]
move=[(0, 1), (0, -1), (1, 0), (-1, 0)]

b=len(rocks)

ans=0

def dfs(grid):
    q=[(r[i], c[i]) for i in range(k)]
    for i in range(k):
        visited[r[i]][c[i]]=True
    ans=len(q)
    while q:
        nowx, nowy=q.pop()
        for dx, dy in move:
            tmpx, tmpy=nowx+dx, nowy+dy
            if 0<=tmpx<n and 0<=tmpy<n:
                if not grid[tmpx][tmpy] and not visited[tmpx][tmpy]:
                    q.append((tmpx, tmpy))
                    visited[tmpx][tmpy]=True
                    ans+=1
    return ans

for bit in range(1<<b):
    if bin(bit).count("1")<b-m:
        continue
    tmpgrid=copy.deepcopy(grid)
    visited=[[False for _ in range(n)] for _ in range(n)]
    for i in range(b):
        if not bit & (1<<i):
            rr, rc=rocks[i]
            tmpgrid[rr][rc]=0
    ans=max(ans, dfs(tmpgrid))

print(ans)