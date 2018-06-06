n=str(input())
digit=0
for i in n:
    if(i.isnumeric()):
        digit += 1
print(digit)
