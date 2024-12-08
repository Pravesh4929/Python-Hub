# 10. Using a Dictionary to Simulate Addition
operations = { "add": lambda x, y: x + y }
x = int(input("Enter the first number: "))
y = int(input("Enter the second number: "))
print("The sum is:", operations["add"](x, y))

