# 1. Write a program to accept two numbers from the user and perform division. If any exception occurs, print an error message or else print the result.
try:
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    result = num1 / num2
    print("Result:", result)
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")
except ValueError:
    print("Error: Please enter valid numbers.")

# 2. Write a program to accept a number from the user and check whether it’s prime or not. If user enters anything other than number, handle the exception and print an error message.
try:
    num = int(input("Enter a number: "))
    if num > 1:
        for i in range(2, num):
            if num % i == 0:
                print(num, "is not a prime number.")
                break
        else:
            print(num, "is a prime number.")
    else:
        print(num, "is not a prime number.")
except ValueError:
    print("Error: Please enter a valid integer.")


# 3. Write a program to accept the file name to be opened from the user, if file exist print the contents of the file in title case or else handle the exception and print an error message.
try:
    file_name = input("Enter the file name: ")
    with open(file_name, "r") as file:
        content = file.read()
        print("Contents of the file in title case:")
        print(content.title())
except FileNotFoundError:
    print("Error: File not found.")
except Exception as e:
    print("Error:", e)


# 4. Declare a list with 10 integers and ask the user to enter an index. Check whether the number in that index is positive or negative number. If any invalid index is entered, handle the exception and print an error message.
try:
    numbers = [1, -2, 3, -4, 5, -6, 7, -8, 9, -10]
    index = int(input("Enter an index (0-9): "))
    if 0 <= index < len(numbers):
        if numbers[index] > 0:
            print(f"The number at index {index} is positive.")
        else:
            print(f"The number at index {index} is negative.")
    else:
        print("Error: Invalid index. Please enter an index between 0 and 9.")
except ValueError:
    print("Error: Please enter a valid integer.")