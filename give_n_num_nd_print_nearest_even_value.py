n=int(input())
a=[]
for i in range(1,n+1):
    if(i%2==0):
        a.append(i)

print (''.join(map(str, a[-1:])))
