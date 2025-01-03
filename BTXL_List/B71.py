'''
Nhập vào một list L có các phần tử là chuỗi 
(các chuỗi này không có ký tự đặc biệt, dấu câu, ký tự số, chỉ có ký tự chữ cái và khoảng trắng)

Hãy tìm ra vị trí của chuỗi có nhiều từ nhất
'''

ds = input('input: ')
ds = ds.split(' ')

def count_max(ds):
    count =  []
    count_value = []
    max = None
    for i in ds:
        check = True
        for y in range(len(count_value)):
            if i==count_value[y]:
                index = y
                check = False
                break
        if check:
            count_value += [i]
            count += [1]
        else: 
            count[index] = count[index] + 1

    for i in range(len(count)):
        if max == None or count[i]>max:
            max = count[i]
            index = i
    return count_value[index]

def count_max1(ds):
    ds1 = []
    max = index = 0
    result = None
    for i in ds:
        index = 0
        if not(i in ds1):
            for y in ds:
                if i==y:
                    index+=1
            ds1+=[i]
        else:
            continue
        if max<index:
            max = index
            result = i
    return result

            
print(count_max1(ds))