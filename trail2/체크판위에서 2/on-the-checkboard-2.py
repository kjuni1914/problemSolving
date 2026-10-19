R, C = map(int, input().split())
grid = [list(input().split()) for _ in range(R)]

# Please write your code here.
    
tmp=[]
for r in range(1, R-2):
    for c in range(1, C-2):
        if grid[r][c]!=grid[0][0]: tmp.append((r, c))

tmp2=[]
while tmp:
    nowr, nowc=tmp.pop()
    for r in range(nowr+1, R-1):
        for c in range(nowc+1, C-1):
            if grid[r][c]!=grid[nowr][nowc]: tmp2.append((r, c))

if grid[R-1][C-1]==grid[0][0]:
    print(0)
else:
    print(len(tmp2))