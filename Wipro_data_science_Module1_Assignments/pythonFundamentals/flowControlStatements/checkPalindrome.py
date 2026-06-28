# Write a program to find if the given number is a palindrome or not.
# Example 1: I/P: 110011 → O/P: 110011 is a palindrome.
# Example 2: I/P: 1234 → O/P: 1234 is not a palindrome.
number = int(input("Enter a number: "))
original_number = number
reverse = 0

while number > 0:
    digit = number % 10
    reverse = reverse * 10 + digit
    number //= 10

if original_number == reverse:
    print(f"{original_number} is a palindrome.")
else:
    print(f"{original_number} is not a palindrome.")