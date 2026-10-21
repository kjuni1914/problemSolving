n = int(input())
num = list(map(int, input().split()))

# Please write your code here.

collected=[]
total=sum(num)
ans=float("inf")

def devide(st, summation):
    global ans
    if len(collected)==n:
        ans=min(ans, abs(total-2*summation))

        return
    for i in range(st, 2*n):
        collected.append(num[i])
        devide(i+1, summation+num[i])
        collected.pop()


devide(0, 0)

print(ans)