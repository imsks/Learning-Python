class Product:
    def __init__(self, name, price, stock_quantity):
        self.name = name
        self.price = price
        self.stock_quantity = stock_quantity

    def calculate_discount(self, discount_percentage):
        discount_amount = self.price * discount_percentage / 100
        return self.price - discount_amount
    