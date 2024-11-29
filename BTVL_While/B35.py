'''
Nhập n

Cho S(k) = 1 + 2 + 3 + … + k

Tìm k sao cho S(k) lớn nhất nhưng nhỏ hơn n
'''

n = int(input('nhập n: '))
k=0
i=1
while k<n:
    k+=i
    if k>=n:
        k-=i
        break
    i+=1

print(k)