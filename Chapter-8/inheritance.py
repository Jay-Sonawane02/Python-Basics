class Car:
    def __init__(self):
        self.car = 'car'
        print("Inside car")

    @staticmethod
    def func():
        print("car function")

    def func2(self):
        print("non static car function")


class Toyota(Car):
    def __init__(self,name):
        self.name = name
     

c1 = Toyota("fortuner")
c1.func()
c1.func2()
