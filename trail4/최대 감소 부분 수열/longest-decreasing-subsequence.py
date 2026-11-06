n = int(input())
m = list(map(int, input().split()))

dp=[0]*10001
ans=0

for i in range(n):
    dp[m[i]]=max(dp[m[i]+1:])+1
    ans=max(dp[m[i]], ans)

print(ans)