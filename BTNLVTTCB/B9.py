# Nhập vào số nguyên a, kiểm tra xem a có phải là số chính phương hay không, nếu có thì in ra True, ngược lại in ra False

import math
a=int(input('nhập vào số a: '))
result=math.sqrt(a)%1==0
print(result)