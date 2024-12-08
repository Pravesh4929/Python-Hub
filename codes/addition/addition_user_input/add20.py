# 20. Using collections.Counter()

from collections import Counter

x = int(input("Enter the first number: "))
y = int(input("Enter the second number: "))
counter = Counter([x, y])
print("The sum is:", sum(counter.values()))
