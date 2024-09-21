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
    return class_person(name, lastname, id, age, role)

def main():
    persons_list = []

    while True:
        print("\n1. Agregar una persona")
        print("2. Mostrar todas las personas")
        print("3. Eliminar una persona")
        print("4. Salir")
        
        opcion = input("Elige una opción: ")

        if opcion == "1":
            person = add_person()
            persons_list.append(person)
            print(f"\nLa persona '{person['name']} {person['lastname']}' ha sido agregada.")
        
        elif opcion == "2":
            if persons_list:
                print("\nListado de personas:")
                for i, person in enumerate(persons_list, 1):
                    print(f"{i}. {person['name']} {person['lastname']}, ID: {person['id']}, Edad: {person['age']}, Rol: {person['role']}")
            else:
                print("\nNo hay personas en la lista.")

        elif opcion == "3":
            if persons_list:
                print("\nListado de personas:")
                for i, person in enumerate(persons_list, 1):
                    print(f"{i}. {person['name']} {person['lastname']}, ID: {person['id']}, Edad: {person['age']}, Rol: {person['role']}")
                
                try:
                    indice = int(input("\nIntroduce el número de la persona que deseas eliminar: ")) - 1
                    if 0 <= indice < len(persons_list):
                        eliminado = persons_list.pop(indice)
                        print(f"\nLa persona '{eliminado['name']} {eliminado['lastname']}' ha sido eliminada.")
                    else:
                        print("\nNúmero inválido.")
                except ValueError:
                    print("\nPor favor, introduce un número válido.")
            else:
                print("\nNo hay personas para eliminar.")
        
        elif opcion == "4":
            print("Saliendo del programa...")
            break
        
        else:
            print("\nOpción no válida. Por favor, elige una opción correcta.")

if __name__ == "__main__":
    main()

