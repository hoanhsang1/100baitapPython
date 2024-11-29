# Giải và biện luận phương trình ax + b = 0

a=int(input('nhập vào số a: '))
b=int(input('nhập vào số b: '))

if a==0:
    if b==0:
        print('Phương trình có vô số nghiệm')
    else:
        print('Phương trình vô nghiệm')
else:
    x=-(b/a)
    print(f'{x:.3f}')
