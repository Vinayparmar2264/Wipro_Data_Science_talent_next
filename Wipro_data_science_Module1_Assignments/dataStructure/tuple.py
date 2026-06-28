#1.Write a program to print the 4th element from first and 4th element from last in a tuple.
my_tuple = (10, 20, 30, 40, 50, 60, 70, 80)
print("4th element from first:", my_tuple[3])
print("4th element from last:", my_tuple[-4])

#2.Write a program to check whether an element exists in a tuple or not.
my_tuple = (10, 20, 30, 40, 50, 60, 70, 80)
element = 40
if element in my_tuple:
    print(f"Element {element} exists in the tuple.")
else:
    print(f"Element {element} does not exist in the tuple.")

# 3. Write a program to convert a list into a tuple.
my_list = [1, 2, 3, 4, 5]
my_tuple = tuple(my_list)
print("Converted tuple:", my_tuple)

#4.Write a program to find the index of an item in a tuple.
my_tuple = (10, 20, 30, 40, 50, 60, 70, 80)
item = 50
try:
    index = my_tuple.index(item)
    print(f"Index of element {item} in the tuple: {index}")
except ValueError:
    print(f"Element {item} is not in the tuple.")

# 5. Write a program to replace last value of tuples in a list to 100.
    # Sample List: [(10, 20, 40), (40, 50, 60), (70, 80, 90)]
    # Expected Output: [(10, 20, 100), (40, 50, 100), (70, 80, 100)]
sample_list = [(10, 20, 40), (40, 50, 60), (70, 80, 90)]
new_list = []
for t in sample_list:
    new_tuple = t[:-1] + (100,)
    new_list.append(new_tuple)
print("List with last values replaced (using for loop):", new_list)
