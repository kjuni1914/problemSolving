n = int(input())

dp=[0]*(max(n+1, 5))
dp[0]=1

for i in range(1, n+1):
    dp[i]=(dp[i-2]+dp[i-3])%10007

print(dp[n])