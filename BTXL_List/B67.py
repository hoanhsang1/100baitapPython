'''
Nhập vào một list số nguyên L, 
hãy đưa các số chẵn trong list về đầu list, 
số lẻ về cuối list và các phần tử 0 nằm ở giữa
'''

def list_input():
    len_list = int(input('nhập chiều dài của list muốn nhập vào:'))
    list_result = []
    for i in range(len_list):
        print('nhập giá trị thứ',i)
        list_result.append(int(input()))
    return list_result

def soft_chanle(List):
	chan = []
	le = []
	for i in List:
		if i%2==0:
			chan+=[i]
		else:
			le+=[i]
	return chan+le
a = list_input()
print(soft_chanle(a))
