'''
Viết hàm đưa vào một list số nguyên và một số nguyên dương k. 
Hãy tìm và trả về vị trí của phần tử đầu tiên có giá trị k trong list số nguyên, 
nếu không có thì trả về -1
'''

def list_input():
    len_list = int(input('nhập chiều dài của list muốn nhập vào:'))
    list_result = []
    for i in range(len_list):
        print('nhập giá trị thứ',i)
        list_result.append(int(input()))
    return list_result


def index(ds,a):
    for i in range(len(ds)):
        if ds[i] == a:
            return i
    return -1

print(index(list_input(),2))
