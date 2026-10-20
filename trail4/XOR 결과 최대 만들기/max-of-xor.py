n, m = map(int, input().split())
A = list(map(int, input().split()))

selected=[]
ans=0
res=0
def func(stidx):
    global ans, res
    if len(selected)==m:
        ans=max(ans, res)
        return
    for i in range(stidx, n):
        selected.append(A[i])
        res=res^A[i]
        func(i+1)
        res=res^selected.pop()

func(0)
print(ans)

# Please write your code here.