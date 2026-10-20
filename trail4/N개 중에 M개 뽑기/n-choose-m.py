N, M = map(int, input().split())

nums=[]

def func(start):
    if len(nums)==M:
        print(*nums)
        return

    for i in range(start, N+1):
        nums.append(i)
        func(i+1)
        nums.pop()

func(1)

# Please write your code here.
