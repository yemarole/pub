class Rectangle:
    def __init__(self, width, height):
        self.__width = width
        self.__height = height

    def get_width(self):
        return self.__width

    def get_height(self):
        return self.__height

    def set_width(self, width):
        self.__width = width

    def set_height(self, height):
        self.__height = height

    def calculate_area(self):
        return self.__width * self.__height


new_rectangle = Rectangle(5, 25)
print(new_rectangle.get_width())

new_rectangle.__width = 10  # This will not change the width of the rectangle as __width is a private variable
print(new_rectangle.get_width())

new_rectangle.set_width(10)  # This will change the width of the rectangle
print(new_rectangle.get_width())

print("Area: ", new_rectangle.calculate_area())
