# Given two non-negative values, print true if they have the same last digit, otherwise print false.

# lastDigit(7, 17) → true
# lastDigit(6, 17) → false
# lastDigit(3, 113) → true

def lastDigit(a, b):
    return a % 10 == b % 10

print(lastDigit(7, 17))   # → true
print(lastDigit(6, 17))   # → false
print(lastDigit(3, 113))  # → true