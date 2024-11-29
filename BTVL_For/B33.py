# Nhập vào số nguyên dương a, kiểm tra xem a có phải là số nguyên tố hay không

a = int(input('nhập vào số nguyên dương a: '))
result=True
if a>=2:
    for i in range(2,a):
        if a%i==0:
            result=False
            print('đây không phải là số nguyên tố')
            break
    if result:
        print('đây là số nguyên tố')
else:
    print('đây không phải là số nguyên tố')

