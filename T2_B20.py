tai_khoan = 0
while True:
    s = input("Nhap vao thuong thuc thanh toan va so tien: ")
    if not s:
        break
    values = [x for x in s.split(' ')]
    phuong_thuc = values[0]
    so_tien = int(values[1])
    if (phuong_thuc == 'D'):
        tai_khoan += so_tien
    elif (phuong_thuc == 'W'):
        tai_khoan -= so_tien
    else:
        pass

print(f"So tien trong tai khoan cua ban la: {tai_khoan}")