from collections import deque

n, m = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]

move=[(0, 1), (0, -1), (1, 0), (-1, 0)]



def dfs():
    q=deque([(0, 0)])
    melt=set()
    visited=[[False for _ in range(m)] for _ in range(n)]

    while q:
        nowx, nowy=q.popleft()
        for dx, dy in move:
            tmpx, tmpy=nowx+dx, nowy+dy
            if 0<=tmpx<n and 0<=tmpy<m:
                if a[nowx][nowy]==0 and a[tmpx][tmpy]==1:
                    melt.add((tmpx, tmpy))
                if visited[tmpx][tmpy] or a[nowx][nowy]==1:
                    continue
                visited[tmpx][tmpy]=True
                q.append((tmpx, tmpy))
    return melt

ans=[0, 0]
while 1:
    tmp=dfs()
    if not tmp:
        break
    ans=[ans[0]+1, len(tmp)]
    for x, y in tmp:
        a[x][y]=0
print(*ans)