so_nhi_phan = [s for s in input("Nhap vao day cac so nhi phan:  ").split(',')]
so_chia_het = []
for so in so_nhi_phan:
    so_nguyen = int(so,2)
    if (so_nguyen % 5 == 0):
        so_chia_het.append(so)
print (so_chia_het)