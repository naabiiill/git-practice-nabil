from datetime import date
from utils import add, subtract, multiply

print("Name: Nabil Mahmud")
print("Today's date:", date.today())

try:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))

    print("\n--- Calculator Results ---")
    print("Addition:", add(a, b))
    print("Subtraction:", subtract(a, b))
    print("Multiplication:", multiply(a, b))

except ValueError:
    print("Please enter valid numbers.")