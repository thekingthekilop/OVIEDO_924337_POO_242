# Clase abstracta
class Person:
    def __init__(self, dni, name, lastname, age):
        self.dni = dni
        self.name = name
        self.lastname = name
        self.age = age

class Student(Person):
    def __init__(self, dni, name, lastname, age, code):
        super().__init__(dni, name, lastname, age)
        self.code = code
        self.__subjects = []
        
    def add_subject(self, subject):
        self.__subjects.append(subject)

    def remove_subject(self, subject):
        if subject in self.__subjects:
            self.__subjects.remove(subject)
        else:
            print(f"La asignatura {subject} no está en la lista de asignaturas.")

    def __str__(self):
        return f"Nombre: {self.name}, Codigo: {self.code}, Asignaturas: {self.__subjects}"

class Professor(Person):
    def __init__(self, dni, name, lastname, age, device, desktop):
        super().__init__(dni, name, lastname, age)
        self.device = device
        self.desktop = desktop

    def __str__(self):
        return f"Nombre: {self.name}, Dispositivo: {self.device}, Puesto de Trabajo: {self.desktop}"

Student_1 = Student(1234, "Luis", "Soto", 21, 12233)
Student_1.add_subject("Matemáticas")
Student_1.add_subject("Programación")
Student_1.remove_subject("Historia") 
Student_1.remove_subject("Matemáticas")
Professor_1 = Professor(1234, "Luis", "Soto", 31, "Laptop", 16)

print(Student_1)
print(Professor_1)
