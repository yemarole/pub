class Animal:
    def __init__(self, species):
        self.species = species

    def sound(self):
        print(f"{self.species} makes a sound")


class Dog(Animal):
    def __init__(self, breed):
        super().__init__("Dog")
        self.breed = breed

    def bark(self):
        super().sound()
        print(f"{self.breed} barks")


# poodle = Dog("Poodle")
# poodle.bark()


# multiple inheritance
class A:
    def methodA(self):
        print("Method A")


class B:
    def methodB(self):
        print("Method B")


class C(A, B):
    def methodC(self):
        print("Method C")


# new_class = C()
# new_class.methodA()
# new_class.methodB()


# Multilevel Inheritance
class Vehicle:
    def __init__(self, brand):
        self.brand = brand

    def drive(self):
        print(f"{self.brand} vehicle is being driven")


class Car(Vehicle):
    def park(self):
        print("Car is parked")


class SportsCar(Car):
    def __init__(self, brand, model):
        super().__init__(brand)
        self.model = model

    def race(self):
        print(f"{self.brand} {self.model} is racing")


# sports_car = SportsCar("Ferrari", "F8 Tributo")
# sports_car.drive()


# Exercise
class Employee:
    def __init__(self, name, role):
        self.role = role
        self.name = name

    def work(self):
        print(f"{self.name} is working as a {self.role}")


class Programmer(Employee):
    def __init__(self, name, language):
        super().__init__(name, "Programmer")
        self.name = name
        self.language = language

    def code(self):
        print(f"{self.name} is coding in {self.language}")


Programmer("John", "Python").work()
