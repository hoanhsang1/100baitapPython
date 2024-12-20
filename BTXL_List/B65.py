'''
Người ta định nghĩa một list số nguyên được gọi là “dạng sóng” 
khi tất cả các phần tử đều lớn hơn hoặc nhỏ hơn hai phần tử xung quanh nó.

Nhập vào một list số nguyên L và kiểm tra xem L có phải là list “dạng sóng” hay không, 
nếu có thì ta in ra True, không có thì ta in False
'''

def list_input():
    len_list = int(input('nhập chiều dài của list muốn nhập vào:'))
    list_result = []
    for i in range(len_list):
        print('nhập giá trị thứ',i)
        list_result.append(int(input()))
    return list_result

def song(List):
	for i in range(1,len(List)-1):
		if List[i]>List[i-1] and List[i]>List[i+1]:
			return True
		elif List[i]<List[i-1] and List[i]<List[i+1]:
			return True
		else:
			return False

a = list_input()
print(song(a))
