from collections import deque

n, m = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]

move=[(0, 1), (0, -1), (1, 0), (-1, 0)]

t, last = 0, 0

q=deque([(0, 0)])
visited=[[False for _ in range(m)] for _ in range(n)]
visited[0][0]=True

while 1:
    nxt=[]
    while q:
        nowx, nowy=q.popleft()
        for dx, dy in move:
            tmpx, tmpy=nowx+dx, nowy+dy
            if 0<=tmpx<n and 0<=tmpy<m and not visited[tmpx][tmpy]:
                visited[tmpx][tmpy]=True
                if a[tmpx][tmpy]==1:
                    nxt.append((tmpx, tmpy))
                else: 
                    q.append((tmpx, tmpy))
    if not nxt:
        break    
    t+=1
    last=len(nxt)
    q=deque(nxt)

print(t, last)
