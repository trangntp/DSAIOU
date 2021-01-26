n = int(input("Nhap vao day gia tri can tinh giai thua"))
kq =1
for i in range(2, n+1):
    kq*=i
print(f"Giai thua cua {n} la : {kq}")