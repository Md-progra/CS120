class Product:
    def __init__(self, name, price, amount):
        self.name = name
        self.price = price
        self.amount = amount

    def __str__(self):
        return f'Product: {self.name}, Price: {self.price}, Amount: {self.amount}'

    def get_price(self):
        # Get amount from user input and convert it to an integer
        amount_bought = int(input('Enter the amount you want to buy: '))    

        # Check if there is enough stock
        if amount_bought > self.amount:
            return "Not enough stock available."

        # Calculate the cost with discount based on amount bought
        if amount_bought < 10:
            cost = amount_bought * self.price
        elif 10 <= amount_bought <= 99:
            cost = amount_bought * self.price * 0.90  # 10% discount
        else:  # amount_bought >= 100
            cost = amount_bought * self.price * 0.80  # 20% discount

        return f'Cost of {amount_bought} {self.name} is {cost}'

    def make_purchase(self):
        amount_bought = int(input('Enter the amount that was bought: '))

        # Check if there is enough stock
        if amount_bought > self.amount:
            return "Not enough stock available."

        # Deduct the amount from the stock
        self.amount -= amount_bought
        return f'Purchase successful! {amount_bought} {self.name} bought. Remaining stock: {self.amount}'
    

    # Create an object of the Product class
product1 = Product('Laptop', 500, 500)
print(product1)
print(product1.get_price())
print(product1.make_purchase())
