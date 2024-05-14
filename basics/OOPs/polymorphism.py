class Shape:
    def area():
        raise NotImplementedError("Subclass must implement this")
    
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height
    
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return 3.14 * (self.radius ** 2)
    
rectangle = Rectangle(10, 20)
circle = Circle(5)

print(circle.area())