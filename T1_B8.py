class Person():
    name = ''
    age = 0
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def printPerson(self):
        print(self.name)
        print(self.age)

person1 = Person(input("Nhap vao ten cua ban: "), int(input("Nhap vao so toi cua ban: ")))
print (person1.name)
print (person1.age)