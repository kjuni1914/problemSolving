n, m = map(int, input().split())
points = [tuple(map(int, input().split())) for _ in range(n)]

d=[[0 for _ in range(n)] for _ in range(n)]

for i in range(n):
    ax, ay=points[i]
    for j in range(n):
        bx, by=points[j]
        d[i][j]=((ax-bx)**2+(ay-by)**2)

selected=[]

ans=float("inf")

def calc(st):
    global ans

    if len(selected)==m:
        tmp=[]
        for idx1 in selected:
            for idx2 in selected:
                if idx1==idx2:
                    continue
                tmp.append(d[idx1][idx2])
        ans=min(ans, max(tmp))
        return
    
    for i in range(st, n):
        selected.append(i)
        calc(i+1)
        selected.pop()

calc(0)

print(ans)