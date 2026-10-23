n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

cnt=0
move=[(0,1), (0,-1), (1,0), (-1,0)]
visited=[[False for _ in range(n)] for _ in range(n)]

def dfs(position):
    q=[position]
    visited[position[0]][position[1]]=True
    cnt=1

    while q:
        nowr, nowc=q.pop()
        for dr, dc in move:
            tmpr, tmpc=nowr+dr, nowc+dc
            if 0<=tmpr<n and 0<=tmpc<n:
                if not visited[tmpr][tmpc] and grid[tmpr][tmpc]==grid[nowr][nowc]:
                    visited[tmpr][tmpc]=True
                    cnt+=1
                    q.append((tmpr, tmpc))
    return cnt

ans=[0, 0]

for r in range(n):
    for c in range(n):
        if not visited[r][c]:
            cnt=dfs((r, c))
            ans[1]=max(ans[1], cnt)
            if cnt>=4:
                ans[0]+=1

print(*ans)