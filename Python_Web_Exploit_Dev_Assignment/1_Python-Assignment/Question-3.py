class Calculator():
    def __init__(self, number):
        self.number = number

    def calculate_square(self):
        return self.number ** 2

    def calculate_cube(self):
        return self.number ** 3

number = int(input("Enter a number: "))
calculator = Calculator(number)
print("Square:", calculator.calculate_square())
print("Cube:", calculator.calculate_cube())