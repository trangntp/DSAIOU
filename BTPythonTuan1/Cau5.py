class IOtString(object):
   def __init__(self):
       self.s = ""

   def getString(self):
       self.s = input("Nhập chuỗi:")
   def printString(self):
       print (self.s.upper())

strObj = IOtString()
strObj.getString()
strObj.printString()