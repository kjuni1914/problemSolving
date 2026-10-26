n = int(input())

dp=[0] * max(4, n+1)

dp[0]=1
dp[1]=2
dp[2]=7


for i in range(3, n+1):
    dp[i]=(-dp[i-3]+dp[i-2]+dp[i-1]*3)%int(1e9+7)

print(dp[n])