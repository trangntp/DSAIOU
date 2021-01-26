class In_Hoa():
    def __init__(self):
        self.str = ""
    def get_String(self):
        self.str = input("Nhap vao mot chuoi ky tu: ")
    def print_String(self):
        print(self.str.upper())

myStr = In_Hoa()
myStr.__init__()
myStr.get_String()
myStr.print_String()