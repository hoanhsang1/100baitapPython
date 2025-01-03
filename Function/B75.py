'''
Viết hàm đưa vào 1 số nguyên a, kiểm tra xem a có phải là số Armstrong hay không
'''

def check_Armstrong(a):
    a = str(a)
    k = len(a)
    result = 0
    for i in a:
        result += int(i)**k
    if result == int(a):
        return True
    return False

print(check_Armstrong(370))