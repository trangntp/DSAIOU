lines =  []
while True:
    s = input("Nhap dong : ")
    if s:
        lines.append(s.upper())
    else:
        break
for sentence in lines:
    print (sentence)