'''
Viết hàm đưa vào 2 số nguyên, số nào lớn hơn thì in bảng cửu chương của số đó
'''

def A(a,b):
    if a>b:
        kq = a
    else:
        kq = b
    for i in range(11):
        print(f'{kq} * {i} = {kq*i}')

A(2,4)