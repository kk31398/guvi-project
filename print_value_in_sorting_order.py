n=[]
a=int(input())
for i in range(1,a+1):
    b=input()
    n.append(b)
    n.sort()
print (" ".join(map(str,n)))

