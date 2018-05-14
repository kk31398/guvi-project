x, y= [int(a) for a in input().split()]
for i in range(x+1,y):
   k=0
   for j in range (2,i//2+1):
       if(i%j==0):
           k=k+1;
   if(k<=0):
       print(i,end=" ")

