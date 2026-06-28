# 1. Write a program to read the entire content from a text file and display it to the user.
with open("sample.txt", "r") as file:
    content = file.read()
    print("Content of the file:")
    print(content)

# 2. Write a program to read first n lines from a text file. Get n as user input.
n = int(input("Enter the number of lines to read: "))
with open("sample.txt", "r") as file:
    lines = []
    for _ in range(n):
        line = file.readline()
        if not line:
            break
        lines.append(line)
    print("First", n, "lines of the file:")
    for line in lines:
        print(line, end="")

# 3. Write a program to accept input from user and append it to a text file
user_input = input("Enter text to append to the file: ")
with open("sample.txt", "a") as file:
    file.write(user_input + "\n")


# 4.  Write a program to read contents from a text file line by line and store each line into a list.
with open("sample.txt", "r") as file:
    lines_list = file.readlines()
    print("Lines stored in a list:")
    print(lines_list)


# 5. Write a program to find the longest word from the text file contents, assuming that the file will have only one longest word in it.
with open("sample.txt", "r") as file:
    content = file.read()
    words = content.split()
    longest_word = max(words, key=len)
    print("The longest word in the file is:", longest_word)

# 6. Write a program to count the frequency of a user entered word in a text file.
word_to_count = input("Enter the word to count: ")
with open("sample.txt", "r") as file:
    content = file.read()
    word_count = content.split().count(word_to_count)
    print(f"The word '{word_to_count}' appears {word_count} times in the file.")