class Person:
    def __init__(self, deni, name, age):
        self.__dni = __dni
        self.__name = name
        self.age = age

    def __str__(self):
        return f"Person(name={self.__name}, age={self.age})"

person_1 = Person(1234, "Luis", 20)
print(person_1)

class ProductInventory:
    def __init__(self, product):
        self.product = product
        self.__stock = 0

    def add_stock(self, quantity):
        self.__stock += quantity

    def remove_stock(self, quantity):
        if quantity <= self.__stock:
            self.__stock-= quantity

    def show_stock(self):
        return f"Para el producto {self.product} hay un stock de {self.__stock}"

inventory = ProductInventory("Coca-Cola")
inventory.add_stock(100)
inventory.remove_stock(20)

print(inventory.show_stock())


