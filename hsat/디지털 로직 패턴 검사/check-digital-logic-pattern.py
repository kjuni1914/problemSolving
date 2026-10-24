from collections import defaultdict

digital_logic = input()
K, M = map(int, input().split())

N=len(digital_logic)
pattern=defaultdict(int)
now=digital_logic[-1]+digital_logic[:K-1]
for i in range(K-1, N):
    now=int(now)
    now=(now<<1)%(1<<(K))
    if digital_logic[i]=="1":
        now+=1

    pattern[now]+=1

    if pattern[now]==M:
        ans=1
        break
else:
    ans=0

print(ans)