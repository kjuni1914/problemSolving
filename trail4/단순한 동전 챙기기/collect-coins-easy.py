from collections import deque
import heapq

n = int(input())
grid = [list(input()) for _ in range(n)]

pos=[None for _ in range(11)]


for i in range(n):
    for j in range(n):
        if grid[i][j]==".":
            continue
        else:
            if grid[i][j]=="E":
                grid[i][j]=10
            elif grid[i][j]=="S":
                grid[i][j]=0
            else:
                grid[i][j]=int(grid[i][j])
        pos[grid[i][j]]=(i, j)

cost=[[float("inf") for _ in range(11)] for _ in range(11)]

for i in range(11):
    for j in range(i+1, 11):
        if pos[i] and pos[j]:
            cost[i][j]=abs(pos[i][0]-pos[j][0])+abs(pos[i][1]-pos[j][1])

dp=[[0 for _ in range(4)] for _ in range(11)]

def calc(last, count):
    if dp[last][count]:
        return dp[last][count]
    if count==3:
        dp[last][3]=cost[last][10]
        return dp[last][3]
    else:
        best=float("inf")
        for i in range(last+1, 10):
            best=min(best, calc(i, count+1)+cost[last][i])
        dp[last][count]=best
        return dp[last][count]

calc(0, 0)

print(dp[0][0] if dp[0][0]!=float("inf") else -1)