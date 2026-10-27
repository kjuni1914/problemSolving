n = int(input())

dp=[0]*20

dp[0]=1

for i in range(20):
    for j in range(1, i+1):
        dp[i]+=dp[j-1]*dp[i-j]

print(dp[n])