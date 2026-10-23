n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

move=[(0, 1), (0, -1), (1, 0), (-1, 0)]

ans=[1, 0]

def bfs(threshold, position):
    q=[position]

    while q:
        nowr, nowc=q.pop()

        for dr, dc in move:
            tmpr, tmpc=nowr+dr, nowc+dc
            if 0<=tmpr<n and 0<=tmpc<m:
                if not visited[tmpr][tmpc] and grid[tmpr][tmpc]>threshold:
                    visited[tmpr][tmpc]=True
                    q.append((tmpr, tmpc))


for threshold in range(1, 101):
    visited=[[False for _ in range(m)] for _ in range(n)]
    tmpans=0
    for r in range(n):
        for c in range(m):
            if not visited[r][c] and grid[r][c]>threshold:
                tmpans+=1
                bfs(threshold, (r, c))
    if tmpans>ans[1]:
        ans=[threshold, tmpans]

print(*ans)