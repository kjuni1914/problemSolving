n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]
x = [p[0] for p in points]
y = [p[1] for p in points]

no_skipped=[0 for _ in range(n)]
skipped=[float('inf') for _ in range(n)]

for i in range(1, n):
    nowx, nowy=points[i]
    prex, prey=points[i-1]
    no_skipped[i]=no_skipped[i-1]+abs(nowx-prex)+abs(nowy-prey)
    
    if i>=2:
        preprex, preprey=points[i-2]
        skipped[i]=min(no_skipped[i-2]+abs(nowx-preprex)+abs(nowy-preprey), skipped[i-1]+abs(nowx-prex)+abs(nowy-prey))



    
    
print(min(skipped[-1], no_skipped[-1]))


# Please write your code here.