# Nhập vào một list số nguyên L(cách nhâu bởi dấu phẩy), tìm và in ra giá trị lớn nhất trong L

L = input('nhập vào 1 dãy số: ')

# dùng chuỗi để làm
# pheptinh=''
# max=0
# for i in range(0,len(n)):
#     if n[i].isdigit():
#         pheptinh+=n[i]
#     elif n[i]==' ':
#         if max<int(pheptinh):
#             max=int(pheptinh)
#         pheptinh=''
# print(max)

# dùng list để làm nếu các số cách nhau bởi dấu chấm
a= L.split(',')

max= 0
for i in a:
    if max<int(i):
        max=int(i)
print(max)