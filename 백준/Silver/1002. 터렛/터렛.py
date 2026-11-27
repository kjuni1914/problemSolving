for _ in range(int(input())):
  x1, y1, r1, x2, y2, r2 = map(int, input().split())

  d=((x1-x2)**2+(y1-y2)**2)**(1/2)

  if x1==x2 and y1==y2:
    if r1==r2:
      print(-1)
      continue
    else:
      print(0)
      continue

  if d<r1 or d<r2:
    if abs(r1-r2)<d:
      print(2)
    elif abs(r1-r2)==d:
      print(1)
    elif abs(r1-r2)>d:
      print(0)

  else:
    if r1+r2<d:
      print(0)
    elif r1+r2==d:
      print(1)
    elif r1+r2>d:
      print(2)