'''
Viết hàm đưa vào 1 list số nguyên L và 1 số nguyên dương a. 
Hãy tính và trả về giá trị trung bình của a phần tử đầu tiên trong L
'''

def list_input():
    len_list = int(input('nhập chiều dài của list muốn nhập vào:'))
    list_result = []
    for i in range(len_list):
        print('nhập giá trị thứ',i)
        list_result.append(int(input()))
    return list_result

def sumds(ds,a):
    sum = 0
    for i in range(a):
        sum+=ds[i]
    return sum/a

print(sumds(list_input(),3))