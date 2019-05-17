def giaithua(x):
    if (x == 1):
        return 1
    else:
        return x*giaithua(x-1)

print (giaithua(int(input("Nhap vao so can tim giai thua: "))))