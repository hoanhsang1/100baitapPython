# Nhập vào một chuỗi, hãy đếm xem trong chuỗi có bao nhiêu ký tự in hoa, bao nhiêu ký tự in 
# thường, bao nhiêu ký tự số


n = input('nhập vào 1 chuỗi: ')

# dùng hàm
# hoa= 0
# thuong= 0
# so= 0
# for i in n:
#     if i.isdigit():
#         so+=1
#     elif i.isupper():
#         hoa+=1
#     else:
#         thuong+=1

# print(hoa)
# print(thuong)
# print(so)

# không dùng hàm
def check_so(n):
    if n>='1' and n<='9':
        return True
    return False

def check_hoa(n):
    if n>='A' and n<='Z':
        return True
    return False

def check_thuong(n):
    if n>='a' and n<='z':
        return True
    return False


hoa= 0
thuong= 0
so= 0
for i in n:
    if check_so(i):
        so+=1
    elif check_hoa(i):
        hoa+=1
    else:
        thuong+=1

print(hoa)
print(thuong)
print(so)