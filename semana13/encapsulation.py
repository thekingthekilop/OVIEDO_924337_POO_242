class Person:
    def _init_(self, name, age):
        self.__name = name
        self.__age = age

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        self.__age = age

person_1 = Person("fabian", 25)

print(person_1.age)

person_1.age = 26

print(person_1.age)
