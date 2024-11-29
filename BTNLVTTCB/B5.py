# Nhập vào số nguyên a, nếu a là số chia hết cho 3 và nằm trong khoảng từ 50 - 100 thì in ra True, ngược lại in ra False

a=int(input('nhập vào số a: '))
result=a%3==0 and a>=50 and a<=100
print(result)