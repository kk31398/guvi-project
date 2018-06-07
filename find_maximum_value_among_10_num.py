num=[]
n=10
c=0
for i in range(1,n+1):
    b=int(input())
    if(c<b):
        num.append(b)
        c=b
print(num[-1])
