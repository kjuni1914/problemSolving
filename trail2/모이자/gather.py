n = int(input())
A = list(map(int, input().split()))


ans=[]

for i in range(n):
    tmp=0
    for j in range(n):
        tmp+=A[j]*abs(i-j)
    ans.append(tmp)

print(min(ans))

# Please write your code here.