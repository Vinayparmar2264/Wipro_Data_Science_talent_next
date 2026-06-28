'''You had saved the items and their price details in a text file, which you purchased yesterday from a nearby supermarket.

You need to know:
How many items did you purchase?
How many items are free?
What is the total amount you had to pay?
What is the discount amount?
What is the final amount did you pay after the discount?

Help yourself by writing a Python code to do this. Include necessary code to handle the possible exceptions.

Note:
Data is stored in a text file Purchase-1.txt.
Each line contains one item's details.
Item name and price are separated by a space.
You have to enter the file name during run time.
Sample Input

Purchase-1.txt

Chocolate 50
Biscuit 35
Icecream 50

Discount 5

(There is one blank line before Discount 5.)

Sample Output
Enter the file name: Purchase-1.txt

No of items purchased: 3
No of free items: 0
Amount to pay: 135
Discount given: 5
Final amount paid: 130'''

try:
    filename = input("Enter the file name: ")
    filename = r"D:\Wipro_Assignments\Wipro_MiniProjects_files\\" + filename  # enter the path of the file here

    with open(filename, "r") as file:
        lines = file.readlines()

    items = 0
    free_items = 0
    total = 0
    discount = 0

    for line in lines:
        line = line.strip()

        # Skip blank line
        if line == "":
            continue

        data = line.split()

        if data[0].lower() == "discount":
            discount = int(data[1])
        else:
            price = int(data[1])

            items += 1

            if price == 0:
                free_items += 1
            else:
                total += price

    final_amount = total - discount

    print("No of items purchased:", items)
    print("No of free items:", free_items)
    print("Amount to pay:", total)
    print("Discount given:", discount)
    print("Final amount paid:", final_amount)

except FileNotFoundError:
    print("Error: File not found.")

except ValueError:
    print("Error: Invalid price in file.")

except Exception as e:
    print("Error:", e)