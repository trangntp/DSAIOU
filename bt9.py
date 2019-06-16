try:
    try:
    val = []
    value = []
    print("Nhập vào email của bạn đi: ")
    s=str(input())
    x1=s.rfind('@')
    x2=len(s)
    if x1 > 0 and x1 < x2 -1:
        a = print("Địa chỉ mail của bạn là:", s)
    else:
        raise Exception
    items=[x for x in input("Hãy nhập vào dãy số bảo mật: ").split(",")]
    for p in items:
        intp=int(p)
        if not intp >= 0 or intp <=99:
            value.append(p)
        else:
            raise Exception
    print("Dãy số bảo mật là: ", ','.join(sorted(list(set(items)))))
    print()
    print(s[:x1],'_',','.join(sorted(list(set(items)))))
except:
    print('phải nhập mail có dạng @ và từ 0 đến 99 nhé!')
