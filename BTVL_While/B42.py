'''
Dãy số fibonacci là dãy số được định nghĩa như sau: 1, 1, 2, 3, 5, 8, 13,... với số kế tiếp sẽ bằng tổng hai số trước đó

Nhập vào A, hãy tìm số trong dãy số fibonacci lớn nhất nhưng không vượt quá A
'''

n = int(input('nhập vào số n: '))
f1=1
f2=0
f=f1+f2
while f<=n:
    f=f1+f2
    f1=f2
    f2=f
    if f<=n:
        print(f)