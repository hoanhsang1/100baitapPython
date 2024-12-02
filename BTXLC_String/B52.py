'''
Nhập vào chuỗi a và chuỗi b

Hãy xóa chuỗi b trong chuỗi a rồi in lại chuỗi a ra màn hình (không dùng hàm replace)

Ví dụ:

Chuỗi a: "Xin chào mọi người!"
Chuỗi b: "Xin chào"
Sau khi xóa, chuỗi a: " mọi người!"
'''

a= input('Nhập vào chuỗi a: ')
b= input('Nhập vào chuỗi b: ')
dem= 0
start= 0
for i in range(0,len(a)):
    if b[0]==a[i]:
        start= i
        dem= start
        for y in range(0,len(b)):
            if b[y]==a[dem]:
                dem+=1
            else:
                break
    if dem==len(b)-1:
        break
# dem+=1
if start==0:
    result= a[dem:]
elif start!=0 and dem<len(a):
    result= a[:start]+a[dem:]
else:
    result= a[:start]
print(result)

