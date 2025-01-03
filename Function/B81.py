'''
Viết hàm đưa vào 1 list số nguyên L và 1 số nguyên dương a. 
Hãy tìm và trả về giá trị lớn thứ a trong list L 
(nếu a = 1 thì tìm giá trị lớn nhất, a = 2 thì tìm giá trị lớn nhì, a = 3 thì 
tìm giá trị lớn ba,...)
'''

def list_input():
    len_list = int(input('nhập chiều dài của list muốn nhập vào:'))
    list_result = []
    for i in range(len_list):
        print('nhập giá trị thứ',i)
        list_result.append(int(input()))
    return list_result

def soft(ds):
    for i in range(len(ds)):
        for y in range(i,len(ds)):
            if ds[i]<ds[y]:
                ds[i],ds[y] = ds[y],ds[i]
    return ds

def chose(ds,a):
    ds_new = soft(ds)
    return ds_new[a-1]


print(chose(list_input(),1))