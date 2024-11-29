# n=int(input('nhập số nguyen duong '))
# sum=0
# index=1
# while index<=n:
#     if index%10==0:
#         print(index)
#     else:
#         print(f'{index:<4}',end=' ')
#     sum+=index
#     index+=1
# print('\ntoongr các số là',sum)
    
# while index<=n:
#     if index%2==0:
#         print(f'{index:<4}',end=' ')
#     if index%10==0:
#         print()
#     index+=1


n= int(input('nhập số n'))
# print('bảng cửu chương',n)
#i=1
# while i<=10:
#     print(n,'*',i,'=',n*i)
#     i+=1
# i=2
# while i<=n:
#     if i==n:
#         print('đây là số nguyên tố')
#         break
#     if n%i==0:
#         print('đây không phải là số nguyên tố')
#         break
#     i+=1
# y=2
# while i<=n:
#     y=2
#     while y<=i:
#         if i%y==0:
#             break
#         y+=1
#     if y==i:
#         print(y,end=' ')
#     i+=1
sum=0
i=1
while i<n:
    if n%i==0:
        sum+=i
    i+=1
if sum==n:
    print('dây là số hoàn hảo')
else:
    print('dây k phai là số hoàn hảo')

  