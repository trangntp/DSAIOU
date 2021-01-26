import math
c=50
h=30
arr=[]
items=[x for x in input("nhap gitr d: ").split(',')]
for d in items:
    arr.append(str(int(round(math.sqrt(2*c*float(d)/h)))))
print (','.join(arr))