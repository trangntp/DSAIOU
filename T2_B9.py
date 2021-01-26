import math
C = 50
H = 30
item = input("Nhap vao mot day so bat ki duoc nhan cach bang dau',':  ")
items = [x for x in item.split(',')]
Q = []
for D in items:
    Q.append(int(round(math.sqrt((2*C*float(D)/H)))))
print(f"Day la Q: {Q}")