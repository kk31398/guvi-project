n,a,d = input().split()
n=int(n)
a=float(a)
d=float(d)
c=0
sum=0
for i in range(n):
    temp=a+(d*c)
    sum += temp
    c=c+1
print(int(sum))
