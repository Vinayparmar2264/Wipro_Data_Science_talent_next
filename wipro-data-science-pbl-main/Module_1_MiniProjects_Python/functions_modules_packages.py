#  Functions 
'''Write a Python function that accepts a hyphen-separated sequence of colors as input and returns the colors in a hyphen-separated sequence after sorting them alphabetically.

Constraint:
All the colors will be completely in either lower case or upper case.

Sample Input 1:
green-red-yellow-black-white

Sample Output 1:
black-green-red-white-yellow


Sample Input 2:
PINK-BLUE-TAN-PURPLE

Sample Output 2:
BLUE-PINK-PURPLE-TAN'''

def sort_colors(colors):
    color_list = colors.split("-")
    color_list.sort()
    return "-".join(color_list)

colors = input("Enter colors separated by hyphens: ")

print(sort_colors(colors))


#Modules 

'''Create a Python module with the following functions:

Function Name	Task
ispalindrome(name)	Given the user name as input, this function should tell us whether the name is a palindrome or not.
count_the_vowels(name)	Given the user name as input, this function should tell us how many vowels are present in it.
frequency_of_letters(name)	Given the user name as input, this function should tell us how many times each letter appears in the name.

Note: Name will be completely in either lower case or upper case.

Import the module in another Python script and test the functions by passing appropriate inputs.

Sample Input 1
bob
Sample Output 1
Yes it is a palindrome.

No of vowels: 1

Frequency of letters:
b-2, o-1'''

# mymodule.py

def ispalindrome(name):
    if name == name[::-1]:
        print("Yes it is a palindrome.")
    else:
        print("No, it is not a palindrome.")


def count_the_vowels(name):
    vowels = "aeiouAEIOU"
    count = 0

    for ch in name:
        if ch in vowels:
            count += 1

    print("No of vowels:", count)


def frequency_of_letters(name):
    freq = {}

    for ch in name:
        if ch in freq:
            freq[ch] += 1
        else:
            freq[ch] = 1

    print("Frequency of letters:")
    for key, value in freq.items():
        print(f"{key}-{value}")

        