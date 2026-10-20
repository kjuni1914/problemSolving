N, K = map(int, input().split())
positions = list(map(int, input().split()))

end=positions[-1]-positions[0]+1
st=1

while st<end:
    md=(st+end)//2
    covered=0
    cnt=0
    for hole in positions:
        if hole>covered:
            covered=hole+md-1
            if cnt<K:
                cnt+=1
            else:
                st=md+1
                break
    else:
        end=md

print(st)
        


