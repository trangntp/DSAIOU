import re
s = input('Nhập mật khẩu: ').split(',')
d = []

for i in s:
    if len(i) < 6 or len(i) > 12:
        continue
    else:
        pass
    if not re.search('[a-z]', i):
        continue
    elif not re.search('[A-Z]', i):
        continue
    elif not re.search('[0-9]', i):
        continue
    elif re.search('\s', i):
        continue
    else:
        pass
    d.append(i)

print(','.join(d))



