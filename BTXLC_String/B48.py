'''
Nhập vào một chuỗi, hãy tách toàn bộ ký tự số trong chuỗi ra rồi tính tổng của chúng

VD:

Nhập chuỗi: abd45ecf47wde3s1
Tổng: 4 + 5 + 4 + 7 + 3 + 1 = 24
'''

n = input('nhập vào 1 chuỗi: ')

sum=0
for i in n:
    if i.isdigit():
        sum+=int(i)
print(sum)