class newclass(object):
    def __init__(self):
        self.s=""
    def getstring(self):
        self.s=input("nhap chuoi: ")
    def printstring(self):
        print(self.s.upper())
str=newclass()
str.getstring()
str.printstring()