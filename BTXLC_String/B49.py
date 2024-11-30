chuoi=input('nhập 1 chuỗi: ')
a=''
i=0
sum=0
while i<len(chuoi):
    if chuoi[i].isnumeric():
        a+=chuoi[i]
        i+=1
    else:
        i+=1
        if a!='':
            sum=sum+int(a)
        a=''

if a!='':
    sum=sum+int(a)



print(sum)