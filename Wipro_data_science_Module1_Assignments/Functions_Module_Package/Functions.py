# 1. Write a function to return the sum of all numbers in a list.
# Sample List: (8, 2, 3, 0, 7)
# Expected Output: 20
def sum_of_numbers(numbers):
    sum_of_numbers = 0
    for i in range(len(numbers)):
        sum_of_numbers += numbers[i]
    return sum_of_numbers   

sample_list = (8, 2, 3, 0, 7)
print("Sum of numbers:", sum_of_numbers(sample_list))

# 2. Write a function to return the reverse of a string.
# Sample String: "1234abcd"
# Expected Output: "dcba4321"
def reverse_string(string):
    reversed_string = ""
    for i in range(len(string) - 1, -1, -1):
        reversed_string += string[i]
    return reversed_string

sample_string = "1234abcd"
print("Reversed string:", reverse_string(sample_string))

# 3. Write a function to calculate and return the factorial of a number (a non-negative integer).
# Sample Input: 5
# Expected Output: 120
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

sample_input = 5
print("Factorial of", sample_input, "is", factorial(sample_input))

# 4. Write a function that accepts a string and prints the number of upper case letters and lower case letters in it.
# Sample String: "Hello World!"
# Expected Output:  Upper case letters: 2, Lower case letters: 8
def count_case_letters(string):
    upper_count = 0
    lower_count = 0
    for char in string:
        if char.isupper():
            upper_count += 1
        elif char.islower():
            lower_count += 1
    print("Upper case letters:", upper_count)
    print("Lower case letters:", lower_count)

sample_string = "Hello World!"
count_case_letters(sample_string)

# 5. Write a function to print the even numbers from a given list. List is passed to the function as an argument.
# Sample List: [1, 2, 3, 4, 5, 6, 7, 8, 9]
# Expected Result: [2, 4, 6, 8]
def print_even_numbers(numbers):
    even_numbers = []
    for number in numbers:
        if number % 2 == 0:
            even_numbers.append(number)
    return even_numbers

sample_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print("Even numbers:", print_even_numbers(sample_list))


# 6. Write a function that takes a number as a parameter and checks whether the number is prime or not.
# Sample Input: 29
# Expected Output: 29 is a prime number.
def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True

sample_input = 29
if is_prime(sample_input):
    print(sample_input, "is a prime number.")
else:
    print(sample_input, "is not a prime number.")