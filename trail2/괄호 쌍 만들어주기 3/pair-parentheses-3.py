A = input()

N=len(A)

# Please write your code here.
ans=0

for i in range(N):
    if A[i]==")": continue

    for j in range(i+1, N):
        if A[j]==")": ans+=1

print(ans)