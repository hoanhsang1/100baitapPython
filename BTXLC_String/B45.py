'''
Nhập vào một chuỗi có dạng 3 số nguyên, mỗi số nguyên cách nhau một dấu phẩy, hãy tính tổng 3 số nguyên đó

VD:

Nhập: 3, 12, 15
Tổng: 30
'''

n = input('nhập vào 1 chuỗi: ')

# cách 1 dùng hàm
# cut= n.split(', ')
# sum= 0
# for i in cut:
#     sum+=int(i)
# print(sum)

# cách 2 
def check(n):
    if n=='1' or n=='2' or n=='3' or n=='4' or n=='5' or n=='6' or n=='7' or n=='8' or n=='9':
        return True
    return False

def cat(n):
    result=''
    for i in n:
        if check(i):
            result+=i
    return result
sum=0
for i in cat(n):
    sum+=int(i)

print(sum)