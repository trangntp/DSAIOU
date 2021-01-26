n = int(input("Nhap vao mot so nguyen de tinh giai thua"))
kq = 1
def TinhGiaiThua(x):
    if(x == 1):
        return 1
    else:
        return x * TinhGiaiThua(x-1)
kq =TinhGiaiThua(n)
print(f"Giai Thua Cua {n} la: {kq}")
