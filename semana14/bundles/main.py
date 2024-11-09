from models.student import Student
from models.professor import Professor

person_1 = Student(
    name = "Luis",
    lastname = "Diaz",
    age = 25,
    code = 924337
)

print(person_1.sayHello())

profesor_1 = Professor(
    name = "James",
    lastname = "Rodriguez",
    age = 33

)

print(profesor_1.sayHello())
