# 19. Using functools.reduce()
from functools import reduce

numbers = list(map(int, input("Enter two numbers separated by space: ").split()))
result = reduce(lambda x, y: x + y, numbers)
print("The sum is:", result)
