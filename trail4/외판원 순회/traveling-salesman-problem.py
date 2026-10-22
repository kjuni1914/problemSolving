n = int(input())
A = [list(map(int, input().split())) for _ in range(n)]


visited=set()
ans=float("inf")

def solve(init, idx, s):
    global ans
    visited.add(idx)

    if len(visited)==n:
        if A[idx][init]:
            ans=min(ans, s+A[idx][init])
    else:
        for i in range(n):
            if i in visited or not A[idx][i]:
                continue
            solve(init, i, s+A[idx][i])

    visited.remove(idx)

solve(0, 0, 0)


print(ans)
