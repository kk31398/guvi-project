val=[]
n=int(input())
k=int(input())
print("\n")

for x in range(n):
    no=int(input())
    val.append(no)
print(val)
print(sum(val[0:k]))
