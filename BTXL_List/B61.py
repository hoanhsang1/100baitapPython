def list_input():
    len_list = int(input('nhập chiều dài của list muốn nhập vào:'))
    list_result = []
    for i in range(len_list):
        print('nhập giá trị thứ',i)
        list_result.append(input())
    return list_result

def softMin(List):
	List = list(map(int,List))
	result = []
	if List==[]:
		return []
	else:
		lList = len(List)
		for i in range(lList):
			if result==[]:
				result += List[i]
			else:
				for y in range(len(result)):
					if List[i]<result[y]:
						result = result[:y]+[List[i]]+result[y:]
						break
					elif y==len(result)-1:
						result+=List[i]
	return result
					
			
def softMin_Lite(n):
	for i in range(len(n)):
		for j in range(i+1,len(n)):
			if n[i]>n[j]:
				a = n[i]
				n[i] = n[j]
				n[j] =  a
	return n


a = list_input()
print(softMin_Lite(a))
