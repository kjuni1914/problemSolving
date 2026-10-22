n = int(input())
A = [list(map(int, input().split())) for _ in range(n)]


visited=set()
ans=float("inf")

def solve(init, idx, s):
    global ans

    if len(visited)==n:
        if A[idx][init]:
            ans=min(ans, s+A[idx][init])
        return

    for i in range(n):
        if i in visited or not A[idx][i]:
            continue
        
        visited.add(i)
        solve(init, i, s+A[idx][i])
        visited.remove(i)

visited.add(0)
solve(0, 0, 0)


print(ans)
