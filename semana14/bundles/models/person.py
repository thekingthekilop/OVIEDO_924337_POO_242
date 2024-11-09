from abc import ABC, abstractmethod

class Person(ABC):
    def __init__(self, name, lastname, age):
        self.name = name
        self.lastname = lastname
        self.age = age

    @abstractmethod
    def sayHello(self):
        pass

    #     @property
    #     def name(self):
    #         return self.__name

    #     @name.setter
    #     def name(self, name):
    #         self.__name = name
            
    # def __str__(self):
    #     return f"Person(name={self.__name}, age={self.age})"
