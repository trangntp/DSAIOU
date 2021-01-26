class Person():
    name = ""
    age = 0
    def __init__(self,name,age):
        self.name = name
        self.yearOld = age

person1 = Person
person1.name = input("Write your name: ")
person1.age = int(input("Write your age: "))
print(f"Your name is {person1.name}")
print(f"Your age is {person1.age}")