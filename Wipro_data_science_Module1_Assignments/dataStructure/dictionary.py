# 1. Write a program to add a key and value to a dictionary.
# Sample Dictionary: {0: 10, 1: 20}
# Expected Result: {0: 10, 1: 20, 2: 30}
my_dict = {0: 10, 1: 20}
my_dict[2] = 30
print("Dictionary after adding key-value pair:", my_dict)

# 2. Write a program to concatenate the following dictionaries to create a new one.
# Sample Dictionary:
# dic1 = {1:10, 2:20}
# dic2 = {3:30, 4:40}
# dic3 = {5:50, 6:60}
dic1 = {1: 10, 2: 20}
dic2 = {3: 30, 4: 40}
dic3 = {5: 50, 6: 60}
new_dict = {**dic1, **dic2, **dic3}
print("Concatenated dictionary:", new_dict)

# Method 2: Using the update() method
new_dict2 = {}
new_dict2.update(dic1)
new_dict2.update(dic2)
new_dict2.update(dic3)
print("Concatenated dictionary (Method 2):", new_dict2)

# 3. Write a program to check if a given key already exists in a dictionary.
my_dict = {1: 10, 2: 20, 3: 30}
key = 2
if key in my_dict:
    print(f"Key {key} exists in the dictionary.")
else:
    print(f"Key {key} does not exist in the dictionary.")


# 4. Write a program to iterate over a dictionary using for loop and print the keys alone, values alone and both keys and values.
my_dict = {1: 10, 2: 20, 3: 30}
print("Keys alone:")
for key in my_dict:
    print(key)
print("Values alone:")
for value in my_dict.values():
    print(value)
print("Both keys and values:")
for key, value in my_dict.items():
    print(f"Key: {key}, Value: {value}")

# 5. Write a program to prepare a dictionary where the keys are numbers between 1 and 15 (both included) and the values are square of the keys.
my_dict = {i: i**2 for i in range(1, 16)}
print("Dictionary with keys as numbers and values as their squares:", my_dict)

#6. Write a program to sum all the values in a dictionary, considering the values will be of int type.
my_dict = {1: 10, 2: 20, 3: 30}
total = sum(my_dict.values())
print("Sum of all values in the dictionary:", total)