'''Through command line arguments, three strings separated by space are given to you. Each string is a series of numbers separated by hyphen (-).

You like all the numbers in string 1.
You dislike all the numbers in string 2.
String 3 contains the numbers given to you.

Your initial happiness is 0.

If a number in string 3 is present in string 1, add 1 to your happiness.
If it is present in string 2, subtract 1 from your happiness.
Otherwise, your happiness does not change.

Output your final happiness at the end.

Sample Input 1
3-1 5-7 1-5-3-8
Sample Output 1
1
Explanation
Numbers in string 1: 3, 1
Numbers in string 2: 5, 7
Numbers given to you: 1, 5, 3, 8
+1 for 1
-1 for 5
+1 for 3
8 is in neither list.

Final happiness = 1'''


like = input("Enter liked numbers: ").split("-")
dislike = input("Enter disliked numbers: ").split("-")
numbers = input("Enter given numbers: ").split("-")

happiness = 0

for num in numbers:
    if num in like:
        happiness += 1
    elif num in dislike:
        happiness -= 1

print("Final Happiness:", happiness)


