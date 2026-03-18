"""
Joseph is learning digital logic subject which will be for his next semester.
He usually tries to solve unit assignment problems before the lecture.
Today he got one tricky question. The problem statement is "A positive integer has been
given as an input. Convert decimal value to binary representation.
Toggle all bits of it after the most significant bit including the most significant bit.
Print the positive integer value after toggling all bits".
"""

# Read the positive integer input
n = int(input("Enter the value of N: "))
m = n
print(n)

# Convert decimal to binary representation
s = ""
while n > 0:
    temp = n & 1
    s = str(temp) + s
    n = n >> 1

print(f"Binary of {m} is: {s}")  # d

# Toggle all bits and convert back to decimal
pow = 0
res = 0
for i in range(
    len(s) - 1, -1, -1
):  # range is starting from right most bit which is what it should be
    if s[i] == "0":
        res += 2**pow
    pow += 1

print(res)
