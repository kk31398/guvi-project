a=int(input("Enter numbers:"))
b=int(input("Enter numbers:"))
c=int(input("Enter numbers:"))
if a>b:
    big=a;
else:
    big=b;

if c>big:
    big=c;

print("the largest of the three a=",a,"b=",b,"c=",c,"is",big)
