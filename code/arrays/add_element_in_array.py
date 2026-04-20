"""Add element in an array"""


def solve():
    n = int(input("Enter number of elements: "))
    arr = []

    for i in range(n):
        val = int(input(f"Enter element {i}: "))
        arr.append(val)

    print(f"Initial array: {arr}")

    adder = int(input("Enter element you want to add: "))
    index = int(input("Enter at which position you want to add: "))

    arr.append(0)

    for i in range(len(arr) - 1, index, -1):
        arr[i] = arr[i - 1]
    arr[index] = adder

    print("Updated array: ")
    print(arr)


solve()
