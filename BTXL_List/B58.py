'''
Nhập vào một list số nguyên L, nhập vào số nguyên x, tìm giá trị trong list xa x nhất
'''

L = input('nhập vào 1 chuỗi số nguyên cách nhau bởi dấu phẩy: ')
x = int(input('nhập số nguyên x: '))
def check(L,x):
    L = L.split(',')
    L = list(map(int,L))
    x = L.index(x)
    before = len(L[:x+1])
    after = len(L[x:])
    if before>after:
        return L[0]
    else:
        return L[-1]
print(check(L,x))