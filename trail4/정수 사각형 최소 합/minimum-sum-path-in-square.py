n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

dp=[[0 for _ in range(n)] for _ in range(n)]
dp[0][n-1]=grid[0][n-1]


def cost(position):
    x, y=position
    if not (0<=x<n and 0<=y<n):
        return 1e9
    if dp[x][y]:
        return dp[x][y]
    dp[x][y]=grid[x][y]+min(cost((x-1, y)), cost((x, y+1)))
    return dp[x][y]

cost((n-1, 0))

print(dp[n-1][0])