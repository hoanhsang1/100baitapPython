# Nhập vào số nguyên dương a, in ra bảng cửu chương của a

a = int(input('nhập vào số nguyên dương a: '))
for i in range(11):
    result = a*i
    print(f'{a} * {i} = {result}')