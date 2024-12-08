# 5. Using a Class with a Method
class Addition:
    def add(self, x, y):
        return x + y

x = int(input("Enter the first number: "))
y = int(input("Enter the second number: "))
obj = Addition()
print("The sum is:", obj.add(x, y))
