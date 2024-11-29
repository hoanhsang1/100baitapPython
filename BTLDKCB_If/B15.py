# Nhập vào 3 số thực dương a, b, c. Kiểm tra xem a, b, c có cấu thành độ dài của 1 tam giác được không


a=float(input('nhập vào số a: '))
b=float(input('nhập vào số b: '))
c=float(input('nhập vào số c: '))

if a+b>c and a+c>b and c+b>a:
    print('đây là 1 tam giác')