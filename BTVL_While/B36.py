'''
Nhập vào A, tìm n nhỏ nhất sao cho

1 + 1/2 + 1/3 + 1/4 + ... + 1/n > A
'''

A = int(input('nhập A: '))
k=0
i=1
while k<=A:
    k+=(1/i)
    i+=1

print(f'{k:.3f}')