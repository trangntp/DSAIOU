str=[x for x in input("nhap chuoi: ").split(" ")]
str.sort()
print(" ".join(set(str)))