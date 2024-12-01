'''
Nhập vào một chuỗi, hãy đếm xem trong chuỗi có bao nhiêu từ 
(quy định là chuỗi không có ký tự đặc biệt, không số, không có dấu câu, chỉ có ký tự chữ và khoảng trắng)
'''

n = input('Nhập vào 1 chuỗi: ')

# cách 1 dùng hàm
# print(len(n))

# Cách 2 tự tạo hàm
def dem(n):
    result=0
    for i in n:
        result+=1
    return result
print(dem(n))