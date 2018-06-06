n=str(input())
digit=0
a=n.count(".")
for i in n:
    if(not(i.isnumeric()or i.isalpha()or i.isspace())):
        digit += 1
print(digit-a)
