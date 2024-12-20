'''
Nhập vào một list số nguyên L, 
hãy đếm số lượng giá trị trong list thỏa tính chất: 
“lớn hơn tất cả các giá trị đứng đằng trước nó”
'''

def list_input():
    len_list = int(input('nhập chiều dài của list muốn nhập vào:'))
    list_result = []
    for i in range(len_list):
        print('nhập giá trị thứ',i)
        list_result.append(int(input()))
    return list_result

def tc(List):
	count = 0
	for i in range(len(List)):
		check = 0
		for y in range(i-1,0,-1):
			if List[y]>List[i]:
				check+=1
				break
		if check==0:
			count+=1
	return count


a = list_input()
print(tc(a))
