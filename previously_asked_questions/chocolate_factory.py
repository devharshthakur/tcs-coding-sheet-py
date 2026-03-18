"""
A chocolate factory is packing chocolates into the packets.
The chocolate packets here represent an array of N number of integer values.
The task is to find the empty packets(0) of chocolate and push it to
the end of the conveyor belt(array).

Example 1 : N=8 and arr = [4,5,0,1,9,0,5,0].
Output: [4, 5, 1, 9, 5, 0, 0, 0]
"""


def solve():
    try:
        # Taking number of elements
        n = int(input("Enter the number of elements: "))
        arr = []

        # Taking array elements one by one
        print(f"Enter {n} elements:")
        for _ in range(n):
            arr.append(int(input()))

        # count keeps track of the position where the next non-zero element goes
        count = 0

        # Move all non-zero elements to the front
        for i in range(n):
            if arr[i] != 0:
                arr[count] = arr[i]
                count += 1

        # Fill the remaining space with zeros
        # Note: We start from 'count' to ensure no positions are skipped
        for i in range(count, n):
            arr[i] = 0

        # Print the final array
        print("Resulting array:")
        for element in arr:
            print(element, end=" ")

    except ValueError:
        print("Please enter valid integers.")


solve()
