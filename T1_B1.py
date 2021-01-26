#Tìm các số trong khoảng 2000-3200 chia het cho 7 nhưng khong chia het cho 5
kq = []
for i in range(2000,3200):
        if (i % 7 ==0) and (i % 5 != 0):
            kq.append(i)
print(kq)
