num=int(input())
d={0:'zero',1:'one',2:'two',3:'three',4:'four',5:'five',6:'six',7:'seven',8:'eight',9:'nine',10:'ten'}
for k, v in d.items():
    if(num==k):
        print(v,end=' ')
