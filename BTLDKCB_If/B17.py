# Nhập vào 3 số a, b, c. Hãy sắp xếp 3 số a, b, c theo thứ tự tăng dần rồi in ra lại

a=int(input('nhập vào số a: '))
b=int(input('nhập vào số b: '))
c=int(input('nhập vào số c: '))

if a>b:
    if a>c:
        if b>c:
            print(c,b,a)
        else:
            print(b,c,a)
    else:
        print(b,a,c)
else:
    if b>c:
        if a>c:
            print(c,a,b)
        else:
            print(a,c,b)
    else:
        print(a,b,c)