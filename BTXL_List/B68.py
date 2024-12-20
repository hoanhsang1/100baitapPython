'''
Nhập vào một list số nguyên L, 
hãy biến đổi L bằng cách thay đổi vị trí giữa giá trị nhỏ nhất và lớn nhất
'''

def list_input():
    len_list = int(input('nhập chiều dài của list muốn nhập vào:'))
    list_result = []
    for i in range(len_list):
        print('nhập giá trị thứ',i)
        list_result.append(int(input()))
    return list_result

def change(List):
	min = 0
	max = 0
	for i in range(len(List)):
		if List[min]>List[i]:
			min = i
		if List[max]<List[i]:
			max = i
	List[min],List[max] = List[max],List[min]
	return List
a = list_input()
print(change(a))