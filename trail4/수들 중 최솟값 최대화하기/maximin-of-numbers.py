n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

used=set()
ans=0

def solve(row, tmpmin):
    global ans

    if len(used)==n:
        ans=max(ans, tmpmin)
    
    else:
        for i in range(n):
            if i in used:
                continue
            
            used.add(i)
            solve(row+1, min(grid[row][i], tmpmin))
            used.remove(i)

solve(0, float("inf"))

print(ans)