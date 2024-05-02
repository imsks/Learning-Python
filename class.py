class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_info(self):
        raise NotImplementedError("Subclass must implement this")

class Admin(Person):
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print("Admin Created")

    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}")
    
admin = Admin("Sachin", 25)
admin.display_info()