my_string = input ("Nhap vao mot chuoi du lieu: ")
my_dict ={
     "Upper" : 0,
     "Lower" : 0
}
for c in my_string:
     if c.isupper():
          my_dict["Upper"] += 1
     elif c.islower():
          my_dict["Lower"] += 1
     else:
          pass
print ("Chu hoa : ", my_dict["Upper"])
print ("Chu thuong : ", my_dict["Lower"])