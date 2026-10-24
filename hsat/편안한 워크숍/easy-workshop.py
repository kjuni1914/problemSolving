N, K = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]

move=[(0, 1), (0, -1), (1, 0), (-1, 0)]

dp=[[[float("inf") for _ in range(K)] for _ in range(N)] for _ in range(N)]
ans=float("inf")

for k in range(K):
    for x in range(N):
        for y in range(N):
            if k==0:
                dp[x][y][k]=0
                continue

            candidate=[]
            for dx, dy in move:
                tmpx, tmpy=x+dx, y+dy
                if 0<=tmpx<N and 0<=tmpy<N and 0<grid[tmpx][tmpy]-grid[x][y]<ans:
                    candidate.append(max(grid[tmpx][tmpy]-grid[x][y], dp[tmpx][tmpy][k-1]))
            
            dp[x][y][k]=min(candidate or [float("inf")])

            if k==K-1:
                ans=min(ans, dp[x][y][k])

print(-1 if ans==float("inf") else ans)