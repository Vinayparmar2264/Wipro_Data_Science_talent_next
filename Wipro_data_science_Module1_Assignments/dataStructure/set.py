# 1. Write a program to remove a given item from the set.
my_set = {1, 2, 3, 4, 5}
item_to_remove = 3
my_set.discard(item_to_remove)
print("Set after removing item:", my_set)

# 2. Write a program to create an intersection of sets.
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}
intersection = set1.intersection(set2)
print("Intersection of sets:", intersection)

# 3. Write a program to create an union of sets.
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}
union = set1.union(set2)
print("Union of sets:", union)

# 4. Write a program to find the maximum and minimum value in a set.
my_set = {10, 20, 30, 40, 50}
max_value = max(my_set)
min_value = min(my_set)
print("Maximum value in the set:", max_value)
print("Minimum value in the set:", min_value)

# find manually : method 2
max_manual = None
min_manual = None
for value in my_set:
    if max_manual is None or value > max_manual:
        max_manual = value
    if min_manual is None or value < min_manual:
        min_manual = value
print("Maximum value (manual):", max_manual)
print("Minimum value (manual):", min_manual)