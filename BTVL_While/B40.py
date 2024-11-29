# Nhập vào số nguyên dương n, tính tổng các chữ số của n

n = int(input('Nhập vào số nguyên dương n: '))
sum=0

while n!=0:
    a=n%10
    sum+=a
    n//=10
print(sum)