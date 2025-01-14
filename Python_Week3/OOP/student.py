class Student:
    # initialise your attributes
    def __init__(self, name, age, grade, height):
        self.name = name
        self.age = age
        self.grade = grade
        self.height = height

    # return a string representation of the object
    def __str__(self):
        return f"Name: {self.name}, Age: {self.age}, Grade: {self.grade}, Height: {self.height}"


# Example usage
student1 = Student("John", 21, "A", 178)
student2 = Student("Jane", 20, "B", 165)

# uses the __str__ method
print(student1)

# access the attributes
print(student2.height)
