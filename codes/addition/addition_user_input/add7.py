# 7. Using a Generator
def add_gen():
    x = int(input("Enter the first number: "))
    y = int(input("Enter the second number: "))
    yield x + y

gen = add_gen()
print("The sum is:", next(gen))
