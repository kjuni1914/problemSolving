n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]
INF = float('inf')
ans = INF

values = set()
for row in grid:
    for v in row:
        values.add(v)

for lo in values:
    dp = [[INF] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if grid[i][j] < lo:
                continue
            if i == 0 and j == 0:
                best = grid[i][j]
            else:
                up = dp[i-1][j] if i > 0 else INF
                left = dp[i][j-1] if j > 0 else INF
                best = min(up, left)
            if best < INF:
                dp[i][j] = max(best, grid[i][j])
    if dp[n-1][n-1] < INF:
        ans = min(ans, dp[n-1][n-1] - lo)

print(ans)