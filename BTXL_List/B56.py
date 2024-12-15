'''
Nhập vào một list số nguyên L, tìm và in ra giá trị dương đầu tiên của list, 
nếu không có giá trị dương, ta in ra -1
'''

L = input('nhập vào 1 chuỗi số nguyên cách nhau bởi dấu phẩy: ')
def check(L):
    L = L.split(',')

    for i in range(0,len(L)):
        if int(L[i])>0:
            return i
    return -1
print(check(L))
