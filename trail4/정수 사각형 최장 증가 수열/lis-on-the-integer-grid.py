import sys
sys.setrecursionlimit(int(1e9))

n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

dp=[[0 for _ in range(n)] for _ in range(n)]

move=[(0, 1), (0, -1), (1, 0), (-1, 0)]
            
def f(position):
    x, y=position
    if not dp[x][y]:
        dp[x][y]=1
        for dx, dy in move:
            tmpx, tmpy=x+dx, y+dy
            if 0<=tmpx<n and 0<=tmpy<n and grid[x][y]<grid[tmpx][tmpy]:
                dp[x][y]=max(dp[x][y], 1+f((tmpx, tmpy)))

    return dp[x][y]

ans=0

for x in range(n):
    for y in range(n):
        ans=max(f((x, y)), ans)

print(ans)