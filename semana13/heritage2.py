from abc import ABC

class Person(ABC):
    def _init_(self,name,age):
        self.name=name
        self.age=age

    def _repr_(self):
        return f"name={self.name},age={self.age}"

class Student(Person):
    def _init_(self,name,age,code):
        super()._init_(name,age)
        self.code=code

student_1=Student("fabian",25,12345)
print(student_1)