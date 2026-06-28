# Write a program to print the sum of all the digits of a given number.
number = int(input("Enter a number: "))
sum_of_digits = 0

while number > 0:
    digit = number % 10
    sum_of_digits += digit
    number //= 10

print("The sum of all the digits is:", sum_of_digits)