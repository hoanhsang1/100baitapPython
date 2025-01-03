'''
Viết hàm đưa vào 1 list có các phần tử là chuỗi, 
tìm và trả về chuỗi ngắn nhất trong list
'''

def list_input():
    len_list = int(input('nhập chiều dài của list muốn nhập vào:'))
    list_result = []
    for i in range(len_list):
        print('nhập giá trị thứ',i)
        list_result.append(input())
    return list_result

def find_maxLen(ds):
    max = None
    for i in ds:
        if max == None or len(max)<len(i):
            max = i
    return max

print(find_maxLen(list_input()))