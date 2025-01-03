'''
Viết hàm đưa vào 1 số nguyên a, kiểm tra xem a có phải là số nguyên tố hay không
'''

def nguyenTo(a):
    if a>1:
        for i in range(2,a+1):
            if a==i:
                return True
            if a%i==0:
                break
    return False

print(nguyenTo(1))
            