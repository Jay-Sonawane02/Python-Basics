class Student:
    def __init__(self):
        self.name = input("Enter Name: ")
        self.age = int(input("Enter age: "))


s1 = Student()
print(s1.name)
print(s1.age)