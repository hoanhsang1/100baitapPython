'''
Nhập vào một list số nguyên L, hãy kiểm tra xem L có phải là một cấp số cộng hay không? 
Nếu có thì tìm và in ra công sai, nếu không có thì in ra None
'''

def list_input():
    len_list = int(input('nhập chiều dài của list muốn nhập vào:'))
    list_result = []
    for i in range(len_list):
        print('nhập giá trị thứ',i)
        list_result.append(int(input()))
    return list_result

def capsocong(List):
    congSai = List[1]-List[0]
    for i in range(len(List)-1):
        if congSai != List[i+1]-List[i]:
            return None
    return congSai

lst = list_input()
print(capsocong(lst))