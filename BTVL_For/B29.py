a= int(input('nhập vào số nguyên dương a: '))
if a>=1:
    print(f'Ước của {a}')
    for i in range(1,a+1):
        if a%i==0:
            print(i,end=' ')