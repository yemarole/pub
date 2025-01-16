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

    def get_language(self):
        return self.language

    def set_language(self, language):
        self.language = language

    def code(self):
        super().work()
        print(f"{self.name} is coding in {self.language}")


# employee1 = Programmer("Otis", "Python")
# print(employee1.get_language())
# employee1.set_language("Ruby")
# employee1.code()


#  Exercise 1:
### This code aims to print the numbers from 1 to 5

# for i in range(1, 6):
#     print(i)

# What is wrong with the code? How can you fix it?
# ANSWER: there is nothing wrong with the code


# Exercise 2:
# ### This code is supposed to check if a number is positive or negative

# num = int(input("Enter a number: "))
# if num > 0:
#     print("The number is positive.")
# else:
#     print("The number is negative.")

# # What is wrong with the code? How can you fix it?
# ANSWER: there is nothing wrong with the code


# Exercise 3:
# # ### This code checks if a given string is a palindrome

# word = "hannah"
# reversed_word = word[::-1]
# if word == reversed_word:
#     print("The word is a palindrome.")
# else:
#     print("The word is not a palindrome.")

# What is wrong with the code? How can you fix it? (Use google to find out how to reverse a string!)
# ANSWER: there is nothing wrong with the code


# Exercise 4:
# # ### Modify the class below called Car with a color attribute and a method to print the color.
# # What is wrong with the code? How can you fix it?


# class Car2:

#     def __init__(self, color):
#         self.color = color

#     def print_color(self):
#         print(f"The car color is: {self.color}")


# # ---------------------------------------

# # Create an object of the Car class with color "red" and print its color

# a = Car2("Red")
# a.print_color()
# # code goes here

# # -----------------------------------------
# # What is the purpose of the __init__ method in the Car class? How can you create an object of the Car class with a different color?
# b = Car2("Blue")
# b.print_color()


# Exercise 5:
### Create a class called Rectangle with attributes width and height, and a method to calculate its area
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calculate_area(self):
        return f"The area of your rectangle is: {self.width * self.height}"


###Create an object of the Rectangle class with width 5 and height 3, then calculate and print its area
rectangle = Rectangle(5, 3)
print(rectangle.calculate_area())

# What are the attributes of the Rectangle class? How can you create an object of the Rectangle class with different width and height values
# ANSWER: the attributes of the rectangle class are width and height. You can create an object of the Rectangle class with different width and height values by passing the new values as arguments when creating the object


# Exercise 6:(Intermediate)


### Create a class called Product with attributes name and price, and a method to apply a discount
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price
        self.discount = 0

    def get_discount(self):
        return self.discount

    def set_discount(self, discount):
        if 0 <= self.discount <= 1:
            self.discount = discount
            print(f"Discount value set to: {self.discount * 100}%")
        else:
            print("Discount value must be between 0 and 1")

    def apply_discount(self):
        self.price -= self.price * self.discount
        return f"The final price of {self.name} is: £{self.price:.2f}"


# Hint: self.price -= (self.price * discount)

#### Create an object of the Product class, set the price to 100, apply a 20% discount, and print the final price
jumper = Product("Jumper", 100)
jumper.set_discount(0.2)
print(jumper.apply_discount())
# How can you modify the code to ensure that the discount value is between 0 and 1?
# ANSWER: I modified the set_discount method to check if the discount value is between 0 and 1
