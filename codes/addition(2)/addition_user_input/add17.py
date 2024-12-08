# 17. Using filter() and map()
numbers = list(map(int, filter(lambda x: x.isdigit(), input("Enter two numbers separated by space: ").split())))
result = sum(numbers)
print("The sum is:", result)
