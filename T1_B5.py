class InHoa(object):
    def __init__(self):
        self.my_str = ""
    
    def get_String(self):
        self.my_str = input("Nhap vao day mot chuoi ki tu: ")
        
    def print_String(self):
        print(self.my_str.upper())

character = InHoa()
character.get_String()
character.print_String()