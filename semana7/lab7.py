# 1: Student
# 2: Collaborator
# 3: Security

def class_person(name, lastname, id, age, role):
    return{
        "name": name,
        "lastname": lastname,
        "id": id,
        "age": age,
        "role": role
    }

def show_objet(object_):
    print(object_)

def add_person():
    name = input("Por favor digita el nombre:\n")
    lastname = input("Por favor digita el apellido:\n")
    id = int(input("Digita tu id:\n"))
    age = int(input("Digita tu edad:\n"))
    role = int(input("Digite su rol:\n"))

# Agregar personas a una lista
# Usar un bucle para agregar usuarios haste que el usuario decida no agregar mas
# Imprimir el contenido del listado 