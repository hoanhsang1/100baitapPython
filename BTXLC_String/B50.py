'''
Nhập vào một chuỗi, kiểm tra chuỗi đó có phải là một chuỗi mật khẩu mạnh hay không 
(một chuỗi mật khẩu mạnh cần có ít nhất 1 ký tự đặc biệt, 1 ký tự in hoa, 
1 con số, 1 chữ thường và độ dài phải lớn hơn 6)
'''

n=input('nhập 1 chuỗi: ')
so= 0
hoa= 0
ki_tu= 0
thuong= 0

for i in n:
    if i.isdigit():
        so+=1
    elif i.isupper():
        hoa+=1
    elif i.islower():
        thuong+=1
    else:
        ki_tu+=1
if so and hoa and ki_tu and thuong and len(n)>6:
    print('đây là một chuỗi mật khẩu mạnh')
else:
    print('đây không phải là một chuỗi mật khẩu mạnh')


