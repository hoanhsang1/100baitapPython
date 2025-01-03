'''
Viết hàm đưa vào 1 list số nguyên L và 1 số nguyên dương a. 
Hãy tìm và trả về một list mới có số phần tử là a, 
giá trị các phần tử là các số nguyên tố tìm được trong list L
'''

def list_input():
    len_list = int(input('nhập chiều dài của list muốn nhập vào:'))
    list_result = []
    for i in range(len_list):
        print('nhập giá trị thứ',i)
        list_result.append(int(input()))
    return list_result

def nguyenTo(a):
    if a>1:
        for i in range(2,a+1):
            if a==i:
                return True
            if a%i==0:
                break
    return False

def check(ds,a):
    result = []
    for i in ds:
        if len(result)==a:
            break
        if nguyenTo(i):
            result+=[i]
    return result

print(check(list_input(),3))