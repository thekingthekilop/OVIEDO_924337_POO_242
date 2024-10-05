# class Person:
#     def __init__(self, name, lastname, age, isMarriedwith, naionality="Colombia"):
#         self.name = name
#         self.lastname = lastname
#         self.age = age
#         self.isMarriedwith = isMarriedwith
#         self.naionality = nationality
    
#     # def __str__(self):         Este se utiliza para llamar de manera especfica o puntual
#     #     return f"{sel.name}"

#     def __repr__(self):  # Este se utiliza para llamar forma detallada 
#         return f"Person(name={self.name}, lastname={self.lastname}, age={self.age}, spouse={self.isMarriedwith}, nationality={self.naionality})"



# person1 = Person(name="James", lastname="Rodruiguez", age= "33", isMarriedwith="Daniela Ospina")    # Esto se llama instancia mejor conocida como self
# print(person1)


# class Person:
#     def __init__(self, name:str, lastname:str, age:int):
#         self.name = name
#         self.lastname = lastname
#         self.age = age
#         self.isMarriedwith = None
#         self.naionality = None
    
#     def __str__(self):  
#         return f"name={self.name}, spouse={spouse_name}"

#     # def __repr__(self):  
#     #     return f"Person(name={self.name}, lastname={self.lastname}, age={self.age},spouse={self.isMarriedwith}, nationality={self.naionality})"

#     def get_married(self, person: "Person"):
#         self.isMarriedwith = person

# person1 = Person(name="James", lastname="Rodruiguez", age=33) 
# person2 = Person(name="Luis",lastname="Diaz",age=25)
# person3 = Person(name="Luisa", lastname="Perez", age=24)

# person1.get_married(person3)
# person3.get_married(person1)

# print(person1)

class Person:
    def __init__(self, name:str, lastname:str, age:int):
        self.__name = name
        self.__lastname = lastname
        self.__age = age
    
    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name
    
    def get_lastname(self):
        return self.__lastname

    def set_lastname(self, lastname):
        self.__lastname = lastname 

    def set_age(self,age):
        self.__age = age

    def __repr__(self):
        return f"name={self.get_name()}, lastname={self.get_lastname()}, age={self.__age}"


person_1 = Person(name="James", lastname="Rodruiguez", age=33) 
person_2 = Person(name="Luis",lastname="Diaz",age=25)
person_3 = Person(name="Luisa", lastname="Perez", age=24)

person_1.set_age(28)
print(person_1)





