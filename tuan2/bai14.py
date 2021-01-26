value=[x for x in input("nhap cac so he nhi phan: ").split(",")]
str=[]
for i in value:
 intValue = int(i,2)
 if (intValue%5==0):
     str.append(i)

print(",".join(str))

