# Nhập vào một list số nguyên L, tính giá trị trung bình của list L

def list_input():
    len_list = int(input('nhập chiều dài của list muốn nhập vào:'))
    list_result = []
    for i in range(len_list):
        print('nhập giá trị thứ',i)
        list_result.append(input())
    return list_result


def average(List):
    result = 0
    List = list(map(int,List))
    for i in List:
        result+=i
    length = len(List)
    result = float(f'{result/length:.3f}')
    return result


a = list_input()
print(average(a))