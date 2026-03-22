"""
You are given an array of integers, arr, and an integer k.
Your task is to find and print the maximum number in
each contiguous window of size k.

Sample test case 1:
Input: arr = [1, 3, -1, -3, 5, 3, 6, 7], k = 3
Output: [3, 3, 5, 5, 6, 7]
"""


def solve():
    # Take user inputs
    arr = list(map(int, input("Enter the elements: ").split()))
    k = int(input("Enter the sliding window size: "))
    n = len(arr)
    # Create a result array
    result = [0] * (n - k + 1)

    for i in range(n - k + 1):
        curr_max = arr[i]

        for j in range(i, i + k):
            if arr[j] > curr_max:
                curr_max = arr[j]

        result[i] = curr_max

    for val in result:
        print(val, end=" ")

    print()


solve()
