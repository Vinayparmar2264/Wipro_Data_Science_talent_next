# 1.  Dictionary 

'''Create a dictionary that contains a list of people and one interesting fact about each of them.

Display each person and his or her interesting fact to the screen. Next, change a fact about one of the people. Also add an additional person and corresponding fact. Display the new list of people and facts. Run the program multiple times and notice if the order changes.

Sample output:

Jeff: Is afraid of Dogs.
David: Plays the piano.
Jason: Can fly an airplane.

Jeff: Is afraid of heights.
David: Plays the piano.
Jason: Can fly an airplane.
Jill: Can hula dance.'''


people = {
    "Jeff": "Is afraid of Dogs.",
    "David": "Plays the piano.",
    "Jason": "Can fly an airplane."
}

# Display the original dictionary
print("Original List:")
for person, fact in people.items():
    print(f"{person}: {fact}")

# Change Jeff's fact
people["Jeff"] = "Is afraid of heights."

# Add a new person
people["Jill"] = "Can hula dance."

# Display the updated dictionary
print("\nUpdated List:")
for person, fact in people.items():
    print(f"{person}: {fact}")



# 2.  List

'''Given the participant’s score sheet for your University Sports Day, you are required to find the runner-up score. You have scores. Store them in a list and find the score of the runner-up.

Sample Input:

[2, 3, 6, 6, 5]

Sample Output:

5

Explanation:
Given list is [2, 3, 6, 6, 5]. The maximum score is 6, second maximum is 5. Hence, we print 5 as the runner-up score.'''

scores = [2, 3, 6, 6, 5]

# Remove duplicates
scores = list(set(scores))

# Sort the list
scores.sort()

# Runner-up score
print("Runner-up score:", scores[-2])



#3. Dictionary and List

'''You have a record of n students. Each record contains the student's name, and their percent marks in Math, Physics and Chemistry. The marks can be floating values. You are required to save the record in a dictionary data type.

Student’s name is the key. Marks stored in a list is the value. The user enters a student's name. Output the average percentage marks obtained by that student.

Formula:

Average = (sum of marks) / (number of subjects)

Sample Input:

{
    "Krishna": [67, 68, 69],
    "Arjun": [70, 98, 63],
    "Malika": [52, 56, 60]
}

Sample Output:

Enter a name: Malika
Average percentage mark: 56

Explanation:

Marks for Malika are [52, 56, 60]
Average = (52 + 56 + 60) / 3 = 56'''

students = {
    "Krishna": [67, 68, 69],
    "Arjun": [70, 98, 63],
    "Malika": [52, 56, 60]
}

# Input student name
name = input("Enter a name: ")

# Calculate and display average marks
marks = students[name]
average = sum(marks) / len(marks)

print("Average percentage mark:", average)



# 4. string
'''Given a string of n words, help Alex to find out how many times his name appears in the string.

Constraint:

1 <= n <= 200

Sample Input:

Hi Alex WelcomeAlex Bye Alex.

Sample Output:

3

Explanation:
Alex name appears 3 times in the string.

Hi Alex WelcomeAlex Bye Alex.'''

text = input("Enter the string: ")

# Count occurrences of "Alex"
count = text.count("Alex")

# Display result
print("Number of times Alex appears:", count)