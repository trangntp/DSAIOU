arr=input("nhap chuoi: ")
d={"hoa":0,"thường":0}
for i in arr:
    if i.islower():
        d["thường"]+=1;
    elif i.isupper():
        d["hoa"]+=1;
    else:
        pass
print("số chữ hoa: ",d["hoa"])
print("số chữ thường: ",d["thường"])