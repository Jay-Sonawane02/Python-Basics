class Order:
    def __init__(self,item,price):
        self.item =item
        self.price = price

    def __gt__(self,order2):
        return self.price>order2.price
    
o1 = Order("abc",10)
o2 = Order("def",20)

print(o1>o2)