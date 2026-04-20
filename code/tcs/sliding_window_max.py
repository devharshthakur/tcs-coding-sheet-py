"""
Problem: Sliding Window Maximum
Given an array and a window size k, find the maximum element in each
consecutive window of size k as the window slides through the array.

Example: arr = [1, 3, 1, 2, 0, 5], k = 3
Windows: [1,3,1] [3,1,2] [1,2,0] [2,0,5]
Output: 3 3 2 5

Two approaches:
1. Brute Force: O(n*k) - check all elements in each window
2. Optimal: O(n) - use max heap to track maximum in current window
"""

import heapq


def solve(arr, k):
    """
    Brute force approach: find maximum in each sliding window
    Time: O(n*k) where n is array length
    """
    ans = []
    # Iterate through all possible windows of size k
    for i in range(len(arr) - k + 1):
        maxi = arr[i]
        # Find maximum in current window from index i to i+k
        for j in range(i, i + k):
            maxi = max(maxi, arr[j])
        ans.append(maxi)
    print(*ans)


def optimalSolution(arr, k):
    """
    Optimal approach using max heap
    Time: O(n log n) where n is array length
    Uses negative values since Python has min heap by default
    """
    heap = []
    ans = []

    # Build initial heap with first k elements
    for i in range(k):
        heapq.heappush(heap, (-arr[i], i))
    # First window's maximum
    ans.append(-heap[0][0])

    # Process remaining elements
    for i in range(k, len(arr)):
        # Add new element to heap
        heapq.heappush(heap, (-arr[i], i))
        # Remove elements outside current window
        while heap[0][1] <= i - k:
            heapq.heappop(heap)
        # Current window's maximum is at heap top
        ans.append(-heap[0][0])
    print(*ans)


# Read input array and window size
arr = list(map(int, input().split()))
k = int(input())
# Run both approaches
solve(arr, k)
optimalSolution(arr, k)
