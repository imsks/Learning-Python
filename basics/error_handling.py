# try:
#     num1 = int(input("Enter a number: "))
#     num2 = int(input("Enter another number: "))

#     result = num1 / num2
#     print("Result: ", result)
# except ValueError:
#     print("Input invalid. Please enter a valid integer")
# except ZeroDivisionError:
#     print("Error: Cannot divide by zero.")
# except Exception as e:
#     print("An error occurred: ", e)

def greet(name):
    if not isinstance(name, str):
        raise TypeError("Name must be string")
    print("Hello,", name)

try:
    greet("Alice")
    greet(123)
except TypeError as e:
    print("Error occurred:", e)
    