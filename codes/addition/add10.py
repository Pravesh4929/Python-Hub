#  10. Using a Dictionary to Simulate Addition
a, b = 5, 3
addition = { "add": lambda x, y: x + y }
print(addition["add"](a, b))