input_str = input("Nhập X, Y: ")
dimensions=[int(x) for x in input_str.split(',')]
rowNum=dimensions[0]
colNum=dimensions[1]

multilist = [[col*row for col in range(colNum)]for row in range(rowNum)]


print (multilist)