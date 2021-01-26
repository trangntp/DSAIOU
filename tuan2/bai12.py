line=[]

while True:
    str=input()
    if str:
        line.append(str.upper())
    else:
        break
for sentence in line:
    print(sentence)