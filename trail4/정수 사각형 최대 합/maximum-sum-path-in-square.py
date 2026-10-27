n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

dp=[[0 for _ in range(n)] for _ in range(n)]
dp[0][0]=grid[0][0]

for i in range(n):
    for j in range(n):
        if i==0 and j==0:
            continue
        elif i==0:
            dp[i][j]=grid[i][j]+dp[i][j-1]
        elif j==0:
            dp[i][j]=grid[i][j]+dp[i-1][j]
        else:
            dp[i][j]=grid[i][j]+max(dp[i][j-1], dp[i-1][j])

print(dp[-1][-1])