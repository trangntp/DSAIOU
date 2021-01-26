
import  sys
money =0;
while True:
    c = input("nhap giao dich: ")
    if not c:
        break
    value = c.split(" ")
    char = value[0]
    mountmoney = int(value[1])
    if char == "D":
        money+=mountmoney;
    elif char == "W" and money > mountmoney:
        money-=mountmoney;
    else:
        print("tiền rút lớn hơn tiền có trong thẻ")
    print("tien con trông the la: ",money)