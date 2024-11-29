'''
Nhập điểm toán, văn, anh.

Nếu điểm đúng quy tắc (trong khoảng từ 0 - 10), ta tính điểm trung bình rồi tiến hành xét:

Nếu điểm trung bình lớn hơn hoặc bằng 8, toán hoặc văn lớn hơn hoặc bằng 8 và không có điểm nào dưới 6.5 thì in ra “Học sinh giỏi”
Nếu không đủ điều kiện học sinh giỏi ta xét nếu điểm trung bình lớn hơn hoặc bằng 6.5, toán hoặc văn lớn hơn hoặc bằng 6.5 và không có điểm nào dưới 5 thì in ra “Học sinh khá”
Nếu không đủ điều kiện học sinh khá ta xét nếu điểm trung bình lớn hơn hoặc bằng 5, toán hoặc văn lớn hơn hoặc bằng 5 và không có điểm nào dưới 3.5 thì in ra “Học sinh trung bình”
Nếu không đủ điều kiện học sinh trung bình ta xét nếu điểm trung bình lớn hơn hoặc bằng 3.5, toán hoặc văn lớn hơn hoặc bằng 3.5 và không có điểm nào dưới 2 thì in ra “Học sinh yếu”
Nếu không đủ điều kiện học sinh yếu ta in ra “Học sinh kém”
'''

# Nhập điểm các môn
try:
    toan = float(input("Nhập điểm Toán: "))
    van = float(input("Nhập điểm Văn: "))
    anh = float(input("Nhập điểm Anh: "))

    # Kiểm tra điểm hợp lệ
    if 0 <= toan <= 10 and 0 <= van <= 10 and 0 <= anh <= 10:
        # Tính điểm trung bình
        diem_tb = (toan + van + anh) / 3
        
        # Xét loại học sinh
        if diem_tb >= 8 and (toan >= 8 or van >= 8) and min(toan, van, anh) >= 6.5:
            print("Học sinh giỏi")
        elif diem_tb >= 6.5 and (toan >= 6.5 or van >= 6.5) and min(toan, van, anh) >= 5:
            print("Học sinh khá")
        elif diem_tb >= 5 and (toan >= 5 or van >= 5) and min(toan, van, anh) >= 3.5:
            print("Học sinh trung bình")
        elif diem_tb >= 3.5 and (toan >= 3.5 or van >= 3.5) and min(toan, van, anh) >= 2:
            print("Học sinh yếu")
        else:
            print("Học sinh kém")
    else:
        print("Điểm nhập không hợp lệ! Điểm phải nằm trong khoảng từ 0 đến 10.")
except ValueError:
    print("Vui lòng nhập số hợp lệ!")
