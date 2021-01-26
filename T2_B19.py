my_list = [x for x in input("Nhap vao chuoi cac so: ").split(",") if (int(x)%2 !=0)]
print ("Day so le: ")
print (",".join(my_list))