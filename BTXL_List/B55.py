'''
Nhập vào một list số nguyên L, 
hãy kiểm tra xem tất cả các phần tử trong mảng có bằng nhau hay không, nếu có thì in True, không có thì in False
'''

L = input('nhập vào 1 chuỗi số nguyên cách nhau bởi dấu phẩy: ')
def check(L):
    L = L.split(',')

    for i in L:
        if i!=L[0]:
            return False
    return True
print(check(L))
