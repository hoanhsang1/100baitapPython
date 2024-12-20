'''
Nhập vào một list số nguyên L, Hãy tìm và in ra một vị trí trong L thỏa hai điều kiện: 
có hai giá trị lân cận và giá trị tại vị trí đó bằng tích hai giá trị lân cận. 
Nếu L không tồn tại giá trị như vậy thì in ra - 1
'''

def list_input():
    x=int(input('Nhập kích thước của danh sách'))
    ds=[]
    for i in range(x):
        print('Nhap gia trị thu',i)
        ds.append(int(input()))
    return ds

 
    
def check1(l):
    for i in range(1,len(l)-1):
        if l[i]==l[i-1]*l[i+1]:
            return i
    return  -1
    
danhs=list_input()
print(check1(danhs))