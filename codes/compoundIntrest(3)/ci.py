# Input from the user
P = float(input("Enter the principal amount (P): "))
r = float(input("Enter the annual interest rate in % (r): ")) / 100  # Convert percentage to decimal
n = int(input("Enter the number of times interest is compounded per year (n): "))
t = float(input("Enter the time in years (t): "))

# Calculate total amount and compound interest
A = P * (1 + r / n) ** (n * t)
CI = A - P

# Output results
print(f"Total Amount (A): {A:.2f}")
print(f"Compound Interest (CI): {CI:.2f}")
