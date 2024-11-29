

a= int(input('nhập vào số nguyên dương a: '))
index=0
for i in range(1,a+1):
    if a%i==0:
        index+=1
print(index)