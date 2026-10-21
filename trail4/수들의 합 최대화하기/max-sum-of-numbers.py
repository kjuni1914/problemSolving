n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

using=[False] * n
ans=0

def P(r, tmpSum):
    global ans 
    if r==n:
        ans=max(ans, tmpSum)
        return

    for i in range(n):
        if using[i]: continue
        using[i]=True
        P(r+1, tmpSum+grid[r][i])
        using[i]=False

P(0, 0)
print(ans)