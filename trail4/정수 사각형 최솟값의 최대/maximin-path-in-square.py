n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

dp=[[0 for _ in range(n)] for _ in range(n)]


for x in range(n):
    for y in range(n):
        if x==0 and y==0:
            dp[0][0]=grid[0][0]
        elif x==0:
            dp[x][y]=min(grid[x][y], dp[x][y-1])
        elif y==0:
            dp[x][y]=min(dp[x-1][y], grid[x][y])
        else:
            dp[x][y]=max(min(grid[x][y], dp[x-1][y]), min(grid[x][y], dp[x][y-1]), dp[x][y])

print(dp[-1][-1])
