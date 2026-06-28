# 1. Write a program to create a list of 5 integers and display the list items. Access individual elements through index
my_list = [10, 20, 30, 40, 50]
print("List items:")
for i in range(len(my_list)):
    print(f"Element at index {i}: {my_list[i]}")


# 2. Write a program to append a new item to the end of the list.
my_list.append(60)
print("List items after appending:")
for i in range(len(my_list)):
    print(f"Element at index {i}: {my_list[i]}")

# 3. Write a program to reverse the order of the items in the list.
original_list = [1, 2, 3, 4, 5]
reversed_list = []
i = len(original_list) - 1
while i >= 0:
    reversed_list.append(original_list[i])
    i -= 1
print("Original list:", original_list)
print("Reversed list:", reversed_list)

# 4. Write a program to print the number of occurrences of a specified element in a list.
my_list = [1, 2, 3, 2, 4, 2, 5]
element = 2
count = 0
i = 0
while i < len(my_list):
    if my_list[i] == element:
        count += 1
    i += 1
print(f"The element {element} occurs {count} times in the list.")

# 5. Write a program to append the items of list1 to list2 in the front.
list1 = [1, 2, 3]
list2 = [4, 5, 6]
i = 0
while i < len(list1):
    list2.insert(i, list1[i])
    i += 1
print("List2 after appending items from List1:", list2)

# 6. Write a program to insert a new item before the second element in an existing list.
my_list = [1, 2, 3, 4, 5]
new_item = 10
my_list.insert(1, new_item)
print("List after inserting", new_item, "before the second element:", my_list)

# 7. Write a program to remove the item from a specified index in a list.
my_list = [1, 2, 3, 4, 5]
index = 2
removed_item = my_list.pop(index)
print(f"Item removed from index {index}: {removed_item}")
print("List after removing the item:", my_list)

# 8. Write a program to remove the first occurrence of a specified element from a list.
my_list = [1, 2, 3, 2, 4, 2, 5]
element = 2
my_list.remove(element)
print(f"First occurrence of {element} removed from the list:")
print("List after removing the element:", my_list)