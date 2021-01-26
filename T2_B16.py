my_string = input("Nhap vao mot chuoi so: ")
my_dict ={
    "char": 0,
    "num": 0
}
for c in my_string:
    if c.isdigit():
        my_dict["num"] += 1
    elif c.isalpha():
        my_dict["char"] +=1
    else:
        pass
print ("Ky tu : ",my_dict["char"])
print ("So : ", my_dict["num"])