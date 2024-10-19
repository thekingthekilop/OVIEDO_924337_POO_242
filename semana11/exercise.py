class Person:
    def __init__(self, nombre, edad):
        self.__nombre = nombre
        self.__edad = edad

    def obtener_nombre(self):
        return self.__nombre

    def modificar_nombre(self, nuevo_nombre):
        if nuevo_nombre != self.__nombre: 
            self.__nombre = nuevo_nombre
        else:
            print("Error: el nuevo nombre es igual al actual.")

    def obtener_edad(self):
        return self.__edad

    def modificar_edad(self, nueva_edad):
        if nueva_edad > 0: 
            self.__edad = nueva_edad
        else:
            print("Error: la edad debe ser un número positivo.")

persona1 = Person("Nicolas", 26)

print("Nombre: ", persona1.obtener_nombre())
print("Edad: ", persona1.obtener_edad())

persona1.modificar_nombre("Fabian")
persona1.modificar_edad(30)

print("Nuevo Nombre: ", persona1.obtener_nombre())
print("Nueva Edad: ", persona1.obtener_edad())

persona1.modificar_edad(-5)

