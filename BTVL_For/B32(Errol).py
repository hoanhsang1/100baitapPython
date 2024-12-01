# Nhập vào số nguyên dương a và b, in ước chung lớn nhất của a và b

a = int(input('nhập vào số nguyên dương a: '))
b = int(input('nhập vào số nguyên dương b: '))
max=0
for i in range(1,a+1):
    if i>b:
        break
    if a%i==0 and b%i==0:
        if max<i:
            max=i
print(max)