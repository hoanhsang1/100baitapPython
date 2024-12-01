'''
Viết chương trình in ra hình tam giác có độ cao h được nhập từ bàn phím
Ví dụ: Ta nhập h = 4:

   *
  * *
 *   *
*******
'''

a= int(input('nhập vào 1 số nguyên dương'))

def cai_cay(a):
    space= a
    space_betwnen=-1

    for i in range(0,a,1):
        
        space1=' '*space
        space2=' '*space_betwnen
        last= '*'*(space_betwnen+space+1)
        if i==0:
            print(space1+'*')
        elif i==(a-1):
            print(space1+last)
        else:
            print(space1+'*'+space2+'*')

        space-=1
        space_betwnen+=2

cai_cay(a)