# Nhập vào một list L, hãy tìm và in ra giá trị âm lớn nhất trong L, nếu L không có giá trị âm thì ta in 0

def list_input():
    len_list = int(input('nhập chiều dài của list muốn nhập vào:'))
    list_result = []
    for i in range(len_list):
        print('nhập giá trị thứ',i)
        list_result.append(input())
    return list_result


def fMax_negaNumber(List):
    max = 0
    List = list(map(int,List))
    for i in List:
        if max<i and i<0:
            max = i
        elif max==0 and i<0:
            max = i
    return max


a = list_input()
print(fMax_negaNumber(a))
