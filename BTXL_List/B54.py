'''
Nhập vào một list số nguyên L (cách nhâu bởi dấu phẩy), nhập vào 2 số nguyên dương a và b (a < b < len(L))

Tìm và in ra số nhỏ nhất trong list từ vị trí a đến vị trí b
'''

L = input('nhập vào 1 số nguyên ')
# a = int(input('nhập vào 1 số nguyên dương a: '))
# b = int(input('nhập vào 1 số nguyên dương b: '))
min = 0
l = L.split(',')

l = list(map(int,l))

# dùng vòng lặp
# for i in range(a,b+1):
#     if min>l[i]:
#         min = l[i]

# dùng soft
l.sort()
min = l[0]
print(min)

