# Nhập vào một số nguyên dương n, kiểm tra xem n có phải là số dạng 2^k hay không

n = int(input('Nhập vào số nguyên dương n: '))
k=0
a=0
while a<=n:
    if a==n:
        print(f'{n} là số dạng 2^{k-1}')
        break
    elif a<n:
        a=2**k
    k+=1
