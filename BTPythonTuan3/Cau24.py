from math import sqrt

pos = [0, 0]
while True:
    s = input()
    if not s:
        break
    s = s.split(' ')
    x = s[0]
    y = int(s[1])
    if x == "UP":
        pos[0] += y
    elif x == "DOWN":
        pos[0] -= y
    elif x == "LEFT":
        pos[1] -= y
    elif x == "RIGHT":
        pos[1] += y
    else:
        pass

print(pos)
print(int(round(sqrt(pos[0]**2+pos[1]**2))))
