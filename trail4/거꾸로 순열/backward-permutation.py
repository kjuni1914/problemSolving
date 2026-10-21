n = int(input())

# Please write your code here.

used=[False for _ in range(n)]
nums=[i+1 for i in range(n)]
using=[]

def P():
    if len(using)==n:
        print(*using)
    for i in range(n-1, -1, -1):
        if used[i]:
            continue
        using.append(nums[i])
        used[i]=True
        P()
        using.pop()
        used[i]=False

P()
