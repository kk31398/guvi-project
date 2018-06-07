n=int(input())
a=[]
for i in range(n):
    b=int(input())
    a.append(b)
    c=sum(a[0:])
print(c//n)

