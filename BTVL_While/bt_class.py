#  câu1
# M=int(input('nhập M'))
# s=0
# for i in range(1,M+1):
#     for y in range(1,11):
#         s+=(i*y)
# print(s)

# câu2
# a = int(input("Nhập số nguyên dương a: "))
# b = int(input("Nhập số nguyên dương b: "))
# ucln=0
# if a==0 and b==0:
#     ucln='không xác định(bất kỳ số nguyên dương nào cũng là ước của 0)'
#     bcnn='không xác định'
# elif a==0 or b==0:
#     if a>b:
#         for i in range(1,a+1):
#             if a%i==0 and b%i==0:
#                 ucln=i
#     else:
#         for i in range(1,b+1):
#             if a%i==0 and b%i==0:
#                 ucln=i
#     bcnn='không xác định'
# else:
#     if a>b:
#         for i in range(1,a+1):
#             if a%i==0 and b%i==0:
#                 ucln=i
#     else:
#         for i in range(1,b+1):
#             if a%i==0 and b%i==0:
#                 ucln=i
#     bcnn= abs(a * b) // ucln


# print('ước chung lỡn nhất là',ucln)
# print('bội chung nhỏ nhất là',bcnn)

# câu3
# x=int(input('nhập x: '))
# n=int(input('nhập n: '))
# result=1
# for i in range(1,n+1):
#     result*=x
# print(result)

# cau4
# tich=1
# tong=0
# a= int(input('nhập vào số nguyên: '))
# while a!=0:
#     tinh=a%10
#     a//=10
#     if tinh%2==0:
#         tich*=tinh
#     else:
#         tong+=tinh

# print('Tích các số chẵn là: ',tich)
# print('Tổng các số lẽ là: ',tong)