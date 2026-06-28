# 1. Write a program to count the number of upper and lower case letters in a String.
string = "Hello, World!"
upper_count = 0
lower_count = 0
for char in string:
    if char.isupper():
        upper_count += 1
    elif char.islower():
        lower_count += 1
print("Number of uppercase letters:", upper_count)
print("Number of lowercase letters:", lower_count)

# 2. Write a program that will check whether a given String is Palindrome or not.
string = "racecar"
cleaned_string = ''.join(c.lower() for c in string if c.isalnum())
is_palindrome = cleaned_string == cleaned_string[::-1]
print("Is the string a palindrome?", is_palindrome)

# 3. Given a string, return a new string made of n copies of the first 2 chars of the original string where n is the length of the string. The string length will be >= 2.
# If input is "Wipro" then output should be "WiWiWiWiWi".
string = "Wipro"
n = len(string)
new_string = (string[:2] * n)
print("New string:", new_string)

# 4. Given a string, if the first or last character is 'x', return the string without those 'x' characters, else return the string unchanged.
# If the input is "xHix", then output is "Hi".
string = "xHix"
if string[0] == 'x':
    string = string[1:]
if string[-1] == 'x':
    string = string[:-1]
print("Modified string:", string)

# 5. Given a string and an integer n, return a string made of n repetitions of the last n characters of the string.
# You may assume that n is between 0 and the length of the string inclusive.
# For example, if the inputs are "Wipro" and 3, then the output should be "propropro".
string = "Wipro"
n = 3
result = string[-n:] * n
print("Result:", result)