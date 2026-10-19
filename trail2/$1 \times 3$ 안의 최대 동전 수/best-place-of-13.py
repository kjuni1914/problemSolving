n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
ans=0
for r in range(n):
    for c in range(n-2):
        ans=max(ans, sum(grid[r][c:c+3]))

print(ans)