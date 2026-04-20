"""
Problem: Find Majority Elements
Find all elements that appear at least N/3 times in an array,
where N is the size of the array.

Approach: Using HashMap/Dictionary
1. Count frequency of each element
2. Check which elements appear >= N/3 times
3. Print those elements

Example: arr = [1, 1, 1, 2, 2, 3], N = 6
- 1 appears 3 times (>= 6/3=2) -> print 1
- 2 appears 2 times (>= 2) -> print 2
- 3 appears 1 time (< 2) -> skip
Output: 1 2
"""


def findMajorityElement(arr, N):
    # Build frequency map for string elements
    freq = {}
    for n in arr:
        num = int(n)  # Convert string to integer
        if num in freq:
            freq[num] += 1
        else:
            freq[num] = 1
    # Print all elements with frequency >= N/3
    for key, val in freq.items():
        if val >= N // 3:
            print(key, end=" ")


def findMajorityElementInt(arr, N):
    # Build frequency map for integer elements
    freq = {}
    for num in arr:
        if num in freq:
            freq[num] += 1
        else:
            freq[num] = 1
    # Print all elements with frequency >= N/3
    for key, val in freq.items():
        if val >= N // 3:
            print(key, end=" ")


def input_array_format():
    # Input format: [e1,e2,e3]
    print("\n[e1,e2,e3]")
    # Remove brackets and split by comma
    arr = list(map(str, input().strip("[]").split(",")))
    findMajorityElement(arr, len(arr))


def input_space_separated():
    # Input format: space-separated integers
    print("\nCase 2: space separated")
    arr = list(map(int, input().split()))
    findMajorityElementInt(arr, len(arr))


# Handle both input formats
input_array_format()
input_space_separated()

# Time Complexity: O(n) - single pass to count frequencies + single pass to print results
# Space Complexity: O(n) - for storing frequency map
