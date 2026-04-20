"""
Problem: Find Missing Number
Given an array of n numbers from range [1, n+1] where one number is missing,
find the missing number using the mathematical formula for sum of natural numbers.

Approach:
1. Calculate expected sum of numbers from 1 to n+1: n*(n+1)/2
2. Calculate actual sum of array elements
3. Missing number = Expected sum - Actual sum

Two variants: Integer format and String format input
"""


def getMissingNumIntFormat(arr, size):
    # Calculate sum of all elements in array
    totalSum = 0
    n = size + 1  # Total numbers should be from 1 to n+1
    for num in arr:
        totalSum += num

    # Expected sum of first n+1 natural numbers
    actualSum = int((n * (n + 1)) / 2)
    # Missing number is the difference
    return actualSum - totalSum


def intFormat():
    # Read n (count of elements)
    N = int(input())
    # Read n integers separated by spaces
    arr = list(map(int, input().split()))
    print(getMissingNumIntFormat(arr, N))


def getMissingNumStrFormat(arr, size):
    # Calculate sum of all elements (convert from string to int)
    totalSum = 0
    for num_str in arr:
        num = int(num_str)
        totalSum += num
    n = size + 1  # Total numbers should be from 1 to n+1
    # Expected sum of first n+1 natural numbers
    actualSum = int((n * (n + 1)) / 2)
    # Missing number is the difference
    return actualSum - totalSum


def strFormat():
    # Read n (count of elements)
    N = int(input())
    # Read n integers separated by commas (as strings)
    arr = list(map(str, input().split(",")))
    print(getMissingNumStrFormat(arr, N))


# Run both input format handlers
intFormat()
strFormat()

# Time Complexity: O(n) - single pass through array
# Space Complexity: O(1) - only using variables, not extra data structures
