# Nhập vào số nguyên dương n, đếm xem n có bao nhiêu chữ số chẵn, bao nhiêu chữ số lẻ

n = int(input('Nhập vào số nguyên dương n: '))
le = 0
chan = 0

while n!=0:
    a=n%10
    if a%2==0:
        chan+=1
    else:
        le+=1
    n//=10
print(chan,le)