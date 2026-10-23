n, k, u, d = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]


selected=set()
combs=[]
def select(i):
    if len(selected)==k: 
        combs.append(list(selected or []))
        return 
    
    for idx in range(i, n*n):
        if idx not in selected:
            selected.add(idx)
            select(idx+1)
            selected.remove(idx)

move=[(0, 1), (0, -1), (-1, 0), (1, 0)]

def dfs(q):
    cnt=0
    visited=[[False for _ in range(n)] for _ in range(n)]
    
    for x, y in q:
        visited[x][y]=True
        cnt+=1
    while q:
        nowx, nowy=q.pop()
        for dx, dy in move:
            tmpx, tmpy=nowx+dx, nowy+dy

            if 0<=tmpx<n and 0<=tmpy<n and not visited[tmpx][tmpy]:
                if u<=abs(grid[nowx][nowy]-grid[tmpx][tmpy])<=d:
                    visited[tmpx][tmpy]=True
                    q.append((tmpx, tmpy))
                    cnt+=1
    return cnt

ans=0


select(0)

for comb in combs:
    ans=max(ans, dfs([divmod(i, n) for i in comb]))

print(ans)