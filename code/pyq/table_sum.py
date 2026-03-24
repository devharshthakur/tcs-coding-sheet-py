"""
Given a number N, your task is to calculate and print the sum of the table of N.

Sample test case 1:
Input: N = 10
Output: 550 (Logic: 55 * 10)

Sample test case 2:
Input: N = 68
Output: 3740 (Logic: 55 * 68)
"""


def solve():
    try:
        n = int(input("Enter the value of n: "))

        # A standard table goes from 1 to 10.
        # The sum of numbers 1 to 10 is always 55.

        # Method 1: Direct Logic (Mathematical)
        # Since (1+2+3+4+5+6+7+8+9+10) = 55
        result = n * 55
        print(f"Sum of table is {result}")

    except ValueError:
        print("Enter a valid integer.")


solve()
