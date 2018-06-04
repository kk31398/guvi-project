num=int(input())
a=map(int,str(num))
temp=0
for i in a:
    b=pow(i,3)
    temp=temp+b
if(num==temp):
    print("yes")
else:
    print("no")
