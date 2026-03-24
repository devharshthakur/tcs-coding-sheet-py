"""
Given two integers, a and b, your task is to determine the sum of the cubes of
all numbers in the range from a to b.

Sample test case:
Input: a = 4, b = 9
Output: 1989
(Logic: 4^3 + 5^3 + 6^3 + 7^3 + 8^3 + 9^3)
"""


def solve():
    try:
        a = int(input("Enter value of a: "))
        b = int(input("Enter value of b: "))

        total = sum(i**3 for i in range(a, b + 1))

        print(f"Sum of the cubes from {a} to {b} is: {total}")

    except ValueError:
        print("Enter valid integers")


solve()
