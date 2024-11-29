'''
Nhập vào một dãy số nguyên, ngưng nhập khi người dùng nhập -1.

Sau khi nhập xong, in số lớn nhất, số nhỏ nhất trong những số vừa nhập
'''

n = int(input('nhập số nguyên: '))
max=0

while n!=-1:
    if n>max:
        max=n
    n = int(input('nhập số nguyên: '))
    
print(max)