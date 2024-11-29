# Giải và biện luận phương trình ax^2 + bx + c = 0
import math
a=int(input('nhập vào số a: '))
b=int(input('nhập vào số b: '))
c=int(input('nhập vào số c: '))
denta=b**2-4*a*c
if a==0:
    if b==0:
        if c==0:
            print('Phương trình có vô số nghiệm')
        else:
            print('Phương trình vô nghiệm')
    else:
        x=-(c/b)
        print(f'Phương trình có nghiệm kép {x}')
else:
    if denta>0:
        x1=-(b+math.sqrt(denta)/(2*a))
        x2=-(b-math.sqrt(denta)/(2*a))
        print(f'Phương trình có hai nghiệm phân biệt là {x1} và {x2}')
    elif denta==0:
        x=-(b)/2*a
        print(f'Phương trình có nghiệm kép {x}')
    else:
        print('Phương trình vô nghiệm thực')

