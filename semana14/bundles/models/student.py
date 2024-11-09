from models.person import Person

class Student(Person):
    def __init__(self, name, lastname, age, code):
        super().__init__(name, lastname, age)
        self.code = code

    def __repr__(self):
        return f"Student(name={self.name}, lastname={self.lastname}, age={self.age}, code={self.code})"

    def sayHello(self):
        return f"Hola soy un estudiante y me llamo: {self.name}"
        