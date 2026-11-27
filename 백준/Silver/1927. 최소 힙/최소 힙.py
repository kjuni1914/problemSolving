import heapq
import sys

q=[]

input=sys.stdin.readline

for _ in range(int(input())):
  cmd=int(input())
  if cmd==0:
    if q:
      print(heapq.heappop(q))
    else:
      print(0)
  else:
    heapq.heappush(q, cmd)