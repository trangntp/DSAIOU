value=[x for x in input("nhap cac so: ").split(',')]
kq=[]
for i in value:
  if(int(i)%2!=0):
    kq.append(i)
print(','.join(kq))