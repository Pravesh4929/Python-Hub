# 18. Using a Custom Operator
class AddOperator:
    def __add__(self, other):
        return self.value + other.value

class Number:
    def __init__(self, value):
        self.value = value

x = Number(int(input("Enter the first number: ")))
y = Number(int(input("Enter the second number: ")))
result = x + y
print("The sum is:", result)
