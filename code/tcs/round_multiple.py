"""
Problem: Round to Nearest Multiple
Given two integers x and y, find the nearest multiple of y to x.

Approach:
1. Divide x by y to get the quotient
2. Round the quotient using custom rounding rules (>= 0.5 rounds up)
3. Multiply the rounded quotient back by y to get nearest multiple

Example: x=7, y=3 -> 7/3=2.33 -> rounds to 2 -> 2*3=6
Example: x=8, y=3 -> 8/3=2.66 -> rounds to 3 -> 3*3=9
"""


def custom_round(number):
    # Extract integer part (whole number)
    integer_part = int(number)
    # Extract decimal part (fractional portion)
    decimal_part = number - integer_part

    # If decimal part >= 0.5, round up
    if decimal_part >= 0.5:
        return integer_part + 1
    # Otherwise, round down (return integer part)
    else:
        return integer_part


# Read two integers from input
x = int(input())
y = int(input())
# Divide x by y
nearest = x / y
# Round the quotient using custom rounding
rounded_number = custom_round(nearest)
# Multiply back by y to get the nearest multiple
print(rounded_number * y)

# Time Complexity: O(1)
# Space Complexity: O(1)
