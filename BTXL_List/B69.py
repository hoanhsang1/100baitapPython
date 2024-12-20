'''
Nhập vào một list L có các phần tử bao gồm chuỗi và số nguyên, 
hãy tìm và in ra chuỗi có độ dài lớn nhất và số nguyên có giá trị nhỏ nhất
'''

def list_input():
    len_list = int(input('nhập chiều dài của list muốn nhập vào:'))
    list_result = []
    for i in range(len_list):
        print('nhập giá trị thứ',i)
        list_result.append(input())
    return list_result

def change(List):
	min = chuoi =None
	for i in List:
		if i.isdigit():
			if min==None or min>i:
				min = i
		else:
			if chuoi==None or len(chuoi)<len(i):
				chuoi = i
	return min,chuoi
a = list_input()
print(change(a))