num = int(input())
for i in range(2, int(num/2)):
    if num % i  == 0:
        print("No")
        break
else:
    print("Yes")
