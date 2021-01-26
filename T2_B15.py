value = []
for x in range(1000, 3001):
    strx = str(x)
    if (int(strx[0]) % 2 ==0) and (int (strx[1]) % 2 == 0) and (int(strx[2]) % 2 == 0) and (int(strx[3]) % 2 ==0):
        value.append(x)

print (value)