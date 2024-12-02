'''
Nhập vào một số nguyên, hãy chuyển số sang chuỗi, rồi đặt dấu chấm phân tách mỗi 3 chữ số 
(phân cách phần ngàn) rồi in ra màn hình

VD:

Nhập số: 375469485
Đổi sang chuỗi rồi in ra: 375.469.485
'''

dem= 0
result= ''

# nếu giá trị đầu vào cho là 1 chuỗi
# n= input('nhập vào 1 số nguyên: ')
# for i in n:
#     if dem==3:
#         result+='.'
#         dem=0
#     result+=str(i)
#     dem+=1

# print(result)

# nếu giá trị đầu vào cho là 1 số
n= int(input('nhập vào 1 số nguyên: '))
a=0
while n!=0:
    a=n%10
    if dem==3:
        result+='.'
        dem=0
    
    result+=str(a)
    dem+=1
    n//=10
result= result[::-1]
print(result)
