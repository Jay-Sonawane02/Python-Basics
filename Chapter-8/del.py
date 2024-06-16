class Student:
    def __init__(self,name):
        self.name = name


s1 = Student("Jay")
del (s1.name)

s1.name ="Sonawane"
print(s1.name)