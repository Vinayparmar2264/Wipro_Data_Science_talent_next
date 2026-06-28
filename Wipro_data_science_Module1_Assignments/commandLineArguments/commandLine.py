import sys

# 1. Write a program to accept two numbers as command line arguments and display their sum.
if len(sys.argv) != 3:
    print("Usage: python script.py <number1> <number2>")
    sys.exit(1)

num1 = sys.argv[1]
num2 = sys.argv[2]

if num1.isdigit() and num2.isdigit():
    result = int(num1) + int(num2)
    print("Sum:", result)
else:
    print("Please provide valid numbers.")


# 2. Write a program to accept a welcome message through command line arguments and display the file name along with the welcome message.
if len(sys.argv) != 2:
    print("Usage: python script.py <welcome_message>")
    sys.exit(1)

welcome_message = sys.argv[1]
print("File Name:", sys.argv[0])
print("Welcome Message:", welcome_message)

# 3. Write a program to accept 10 numbers through command line arguments and calculate the sum of prime numbers among them.
if len(sys.argv) != 11:
    print("Usage: python script.py <num1> <num2> ... <num10>")
    sys.exit(1)

sum_of_primes = 0
for i in range(1, 11):
    if sys.argv[i].isdigit():
        num = int(sys.argv[i])
        is_prime = True
        if num > 1:
            for j in range(2, int(num**0.5) + 1):
                if num % j == 0:
                    is_prime = False
                    break
        if is_prime:
            sum_of_primes += num

print("Sum of prime numbers:", sum_of_primes)