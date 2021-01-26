str=input("nhap cau: ")
d={"chữ":0,"số":0}
for x in str:
    if x.isdigit():
        d["số"]+=1
    elif x.isalpha():
        d["chữ"]+=1
    else:
        pass

print("số chữ cái: ",d["chữ"])
print("số chữ số: ",d["số"])

