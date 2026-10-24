N = int(input())

fibo=[0] * 46

fibo[1]=1
fibo[2]=1

def f(idx):
    if not fibo[idx]:
        fibo[idx]=f(idx-1)+f(idx-2)
    return fibo[idx]

f(N)
print(fibo[N])
# Please write your code here.
