'''
Người ta định nghĩa một list số nguyên là list chẵn lẻ, nếu như tổng 2 phần tử bất kỳ bên trong list đều là số lẻ

Nhập vào một list số nguyên L và kiểm tra xem L có phải là list chẵn lẻ hay không
'''

def list_input():
	len_list = int(input('nhập chiều dài của list muốn nhập vào:'))
	list_result = []
	for i in range(len_list):
		print('nhập giá trị thứ',i)
		list_result.append(int(input()))
	return list_result

def chan_le(List):
	sai = 'đây k phải là list chẵn lẽ'
	dung = 'đây là list chẵn lẽ'
	for i in range(len(List)):
		for y in range(i+1,len(List)):
			a = List[i]+List[y]
			if a%2==0:
				return sai
	return dung

a = list_input()
print(chan_le(a))
