# 13. Using a For Loop with a List
numbers = []
for i in range(2):
    numbers.append(int(input(f"Enter number {i+1}: ")))
print("The sum is:", sum(numbers))

