class Person():
    name = ""
    age = 10
    color_pelo = ""
    __numero_telef = ""

    def __init__(self, color, name=None):
        self.name = name
        self.color_pelo = color


persona1 = Person("Negro", "Francisco")
persona1.__numero_telef = "656565656565"

print(persona1.color_pelo, persona1.name, persona1.__numero_telef)


# Herencia
class User(Person):

    def __init__(self, color, name=None):
        super(User, self).__init__(color, name=name)

user1 = User("Rojo", "Juan")
user1.age = 20

print("Hijo ", user1.color_pelo, user1.name, user1.age)
