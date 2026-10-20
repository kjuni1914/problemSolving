a = input()
tmp=""
flag=True
for i in range(len(a)):
    if a[i]=="0" and flag:
        tmp+="1"
        flag=False
    else:
        tmp+="0"
if flag:
    ans=int(a, 2)-1
else:
    ans=int(a, 2)+int(tmp, 2)
    

print((ans))
# Please write your code here.