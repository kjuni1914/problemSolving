n = int(input())

# Please write your code here. 

nums=[i+1 for i in range(n)]
used=[False for _ in range(n)]
using=[]

def P():
    if len(using)==n:
        print(*using)
    for i in range(n):
        if used[i]:
            continue
        used[i]=True
        using.append(nums[i])
        P()
        used[i]=False
        using.pop()


P()