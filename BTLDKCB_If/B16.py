# Từ bài số 15, nếu a, b, c cấu tạo thành được một tam giác, kiểm tra xem đó là tam giác gì 
# (tam giác đều, tam giác vuông cân, tam giác vuông, tam giác cân hay tam giác thường)


a=float(input('nhập vào số a: '))
b=float(input('nhập vào số b: '))
c=float(input('nhập vào số c: '))

if a+b>c and a+c>b and c+b>a:
    if a==b==c:
        print('Đây là tam giác đều')
    elif (a==b or a==c or c==b) and (a**2+b**2==c**2 or a**2+c**2==b**2 or c**2+b**2==a**2):
        print('Đây là tam giác vuông cân')
    elif a==b or a==c or c==b:
        print('Đây là tam giác cân')
    elif a**2+b**2==c**2 or a**2+c**2==b**2 or c**2+b**2==a**2:
        print('Đây là tam giác vuông')
    else:
        print('Đây là tam giác thường')
