# Nhập tháng, năm. Hãy cho biết tháng đó có bao nhiêu ngày
 
month=int(input('nhập vào số tháng: '))
year=int(input('nhập vào số năm: '))
if year%4==0:
    if month==2:
        print(f'tháng {month} có 29 ngày')
    elif month==4 or month==6 or month==9 or month==12:
        print(f'tháng {month} có 30 ngày')
    else:
        print(f'tháng {month} có 31 ngày')
else:
    if month==2:
        print(f'tháng {month} có 28 ngày')
    elif month==4 or month==6 or month==9 or month==12:
        print(f'tháng {month} có 30 ngày')
    else:
        print(f'tháng {month} có 31 ngày')