x=int(input("nhap so: "))
def giaithua(x):
    if(x==1):
        return 1
    return x*giaithua(x-1)
print(giaithua(x))