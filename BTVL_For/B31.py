# Nhập vào số nguyên dương a và b, in toàn bộ ước chung của a và b

a = int(input('nhập vào số nguyên dương a: '))
b = int(input('nhập vào số nguyên dương b: '))
if a>=b:
    for i in range(1,b+1):
        if a%i==0 and b%i==0:
            print(i)
else:
    for i in range(1,a+1):
        if a%i==0 and b%i==0:
            print(i)