# Write a program to reverse a given number and print it.

# Example 1: I/P: 1234 → O/P: 4321
# Example 2: I/P: 1004 → O/P: 4001

number = int(input("Enter a number: "))
reverse = 0

while number > 0:
    digit = number % 10
    reverse = reverse * 10 + digit
    number //= 10

print("The reversed number is:", reverse)