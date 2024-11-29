'''
Nhập vào số nguyên dương n, đếm xem n có bao nhiêu chữ số
'''

n = int(input('Nhập vào số nguyên dương n: '))
index=0
while n!=0:
    index+=1
    n//=10
print(index)