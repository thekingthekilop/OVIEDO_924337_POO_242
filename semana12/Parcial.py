class Libro:
    def __init__(self, titulo, autor, isbn):
        self.__titulo = titulo
        self.__autor = autor
        self.__isbn = isbn
        self.__disponible = True

    def obtener_titulo(self):
        return self.__titulo

    def obtener_autor(self):
        return self.__autor

    def obtener_isbn(self):
        return self.__isbn

    def cambiar_disponibilidad(self, estado):
        self.__disponible = estado

    def esta_disponible(self):
        return self.__disponible

    def __str__(self):
        return f"{self.__titulo} de {self.__autor} (ISBN: {self.__isbn})"

    def __repr__(self):
        return f"Libro('{self.__titulo}', '{self.__autor}', '{self.__isbn}')"

class Miembro:
    def __init__(self, nombre, identificacion):
        self.__nombre = nombre
        self.__identificacion = identificacion
        self.__libros_prestados = []

    def agregar_libro(self, libro):
        if libro.esta_disponible():
            libro.cambiar_disponibilidad(False)
            self.__libros_prestados.append(libro)
            return True
        return False

    def devolver_libro(self, libro):
        if libro in self.__libros_prestados:
            libro.cambiar_disponibilidad(True)
            self.__libros_prestados.remove(libro)
            return True
        return False

    def obtener_prestamos(self):
        return self.__libros_prestados

    def __str__(self):
        return f"Miembro: {self.__nombre} (ID: {self.__identificacion})"

    def __repr__(self):
        return f"Miembro('{self.__nombre}', '{self.__identificacion}')"

class MiembroVIP(Miembro):
    def __init__(self, nombre, identificacion, limite_prestamos=10):
        super().__init__(nombre, identificacion)
        self.__limite_prestamos = limite_prestamos

    def agregar_libro(self, libro):
        if len(self.obtener_prestamos()) < self.__limite_prestamos and libro.esta_disponible():
            return super().agregar_libro(libro)
        return False

    def __str__(self):
        return f"Miembro VIP: {self._Miembro__nombre} (ID: {self._Miembro__identificacion}, Límite: {self.__limite_prestamos})"

    def __repr__(self):
        return f"MiembroVIP('{self._Miembro__nombre}', '{self._Miembro__identificacion}', Límite: {self.__limite_prestamos})"

def prueba_biblioteca():
    libro1 = Libro("1984", "George Orwell", "123456789")
    libro2 = Libro("Cien Años de Soledad", "Gabriel García Márquez", "987654321")
    miembro = Miembro("Juan Pérez", "001")
    miembro_vip = MiembroVIP("María González", "002")

    print(miembro)
    if miembro.agregar_libro(libro1):
        print(f"{miembro} ha prestado {libro1}")
    if miembro.devolver_libro(libro1):
        print(f"{miembro} ha devuelto {libro1}")

    print(miembro_vip)
    if miembro_vip.agregar_libro(libro2):
        print(f"{miembro_vip} ha prestado {libro2}")
    if miembro_vip.devolver_libro(libro2):
        print(f"{miembro_vip} ha devuelto {libro2}")

prueba_biblioteca()
