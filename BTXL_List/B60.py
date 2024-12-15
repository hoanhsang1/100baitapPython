'''
Nhập vào một list số nguyên L, 
hãy kiểm tra xem L có được sắp xếp từ bé đến lớn hay không, nếu có thì in True, không có thì in False
'''

def list_input():
	len_list = int(input('nhập chiều dài của list muốn nhập vào:'))
	list_result = []
	for i in range(len_list):
		print('nhập giá trị thứ',i)
		list_result.append(input())
	return list_result

def check_softMin(List):
	List = list(map(int,List))
	if List==[]:
		return -1
	else:
		for i in range(len(List)):
			if i==0:
				continue
			elif List[i]<List[i-1]:
				return False
	return True


a = list_input()
print(check_softMin(a))