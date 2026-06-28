'''Your friend has sent you a text file containing n lines. He sent a secret message with it, which tells you the place and time where you have to go and meet him.

He challenges you to find it out without seeing the content of the file. He has given hints to find it.

Hints to find the secret message

The number of lines in the file tells you the meeting time.

Note: 1 <= number of lines <= 24

If the number of lines is greater than 12, convert it to 12-hour format.
Example:
If the number of lines is 15, the meeting time is 3 PM.
If the number of lines is 10, the meeting time is 10 AM.

The word appearing the maximum number of times tells you the meeting place.

Note: Meeting place will be a street name.

Example:

If the word Oxford appears the maximum number of times, then the meeting place is Oxford Street.
If the word Park appears the maximum number of times, then the meeting place is Park Street.
Sample Input

Sample.txt

Cricket, a bat-and-ball park game played between two teams of eleven park
players on a field at the park center of which is a 20-metre (22-yard) pitch with
a wicket at each end, each park comprising two bails balanced on three stumps.
The batting park scores runs by striking the ball bowled at the park wicket with
the park bat, while the bowling and park fielding side tries to prevent this and
dismiss each park player (so they are "out"). Means of park include being
bowled, when the ball hits the park and dislodges the bails, and by the fielding
side park the ball after it is hit by the bat, but before it hits the park. When ten
park have been dismissed, the innings ends and the teams park roles.

Sample Output
Meeting time: 9 AM

Meeting place: Park Street

Explanation:

Number of lines = 9 → 9 AM
The word Park appears 15 times → Park Street'''

from collections import Counter
import string

# Read the file
filename = r"D:\Wipro_Assignments\Wipro_MiniProjects_files\sample.txt"

with open(filename, "r") as file:
    lines = file.readlines()


# Find Meeting Time
line_count = len(lines)

if line_count <= 12:
    meeting_time = f"{line_count} AM"
elif line_count == 24:
    meeting_time = "12 AM"
else:
    meeting_time = f"{line_count - 12} PM"


# Find Meeting Place
text = " ".join(lines)

# Remove punctuation
text = text.translate(str.maketrans("", "", string.punctuation))

# Convert to lowercase
words = text.lower().split()

# Count word frequencies
frequency = Counter(words)

# Most frequent word
place = frequency.most_common(1)[0][0].capitalize()

print("Meeting time:", meeting_time)
print("Meeting place:", place + " Street")