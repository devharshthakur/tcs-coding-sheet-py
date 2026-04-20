"""
Question: Find Equilibrium Index

An equilibrium index is an index where the sum of all elements
to the left equals the sum of all elements to the right.
Find the equilibrium index in the given array, or return -1 if none exists.
"""


def solve():
    n = int(input("Enter the number of elelments: "))
    arr = []

    for i in range(n):
        t = int(input(f"Enter element {i}: "))
        arr.append(t)

    left_sum = 0
    left_sum_so_far = [0] * n

    for i in range(n):
        left_sum += arr[i]
        left_sum_so_far[i] = left_sum

    right_sum = 0
    right_sum_so_far = [0] * n

    for i in range(n - 1, -1, -1):
        right_sum += arr[i]
        right_sum_so_far[i] = right_sum

    # Find equilibrium index
    equilibrium_index = -1

    for i in range(n):
        if left_sum_so_far[i] == right_sum_so_far[i]:
            equilibrium_index = i
            break

    if equilibrium_index != -1:
        print(f"Equilibrium index is {equilibrium_index}")
    else:
        print("No Equilibrium index found")


solve()
