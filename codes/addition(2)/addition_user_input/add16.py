# 16. Using Recursion in  python 
def add_recursively(x, y):
    if y == 0:
        return x
    else:
        return add_recursively(x + 1, y - 1)

x = int(input("Enter the first number: "))
y = int(input("Enter the second number: "))
print("The sum is:", add_recursively(x, y))
