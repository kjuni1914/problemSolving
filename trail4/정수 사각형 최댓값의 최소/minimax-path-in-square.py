n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

dp=[[0 for _ in range(n)] for _ in range(n)]




for x in range(n-1, -1, -1):
    for y in range(n-1, -1, -1):

        if x==n-1 and y==n-1:
            dp[x][y]=grid[x][y]
        elif x==n-1:
            dp[x][y]=max(dp[x][y+1], grid[x][y])
        elif y==n-1:
            dp[x][y]=max(dp[x+1][y], grid[x][y])
        else:
            dp[x][y]=min(max(dp[x+1][y], grid[x][y]), max(dp[x][y+1], grid[x][y]))


print(dp[0][0])