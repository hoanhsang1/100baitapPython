n=input('nhập 1 chuỗi: ')
# a=''
# i=0
# sum=0
# while i<len(n):
#     if n[i].isnumeric():
#         a+=n[i]
#         i+=1
#     else:
#         i+=1
#         if a!='':
#             sum=sum+int(a)
#         a=''

# if a!='':
#     sum=sum+int(a)



# print(sum)

a=''
sum=0
for i in n:
    if i.isdigit():
        a+=i
    else:
        if a!='':
            sum+=int(a)
            a=''
if a!='':
    sum=sum+int(a)
print(sum)