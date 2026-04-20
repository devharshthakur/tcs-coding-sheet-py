"""Find smallest number in array"""


def solve():
    n = int(input("Enter minmum number of elements in array: "))
    arr: list[int] = []

    input_str = input(f"Enter {n} elements one by one with space: ")
    str_arr = input_str.split()

    # debug
    print(f"String array is: {str_arr}")

    for i in range(n):
        temp = str_arr[i]
        arr.append(int(temp))

    # debug
    print(f"Number array is: {arr}")

    if n > 0:
        min = arr[0]

        for i in range(1, n):
            if arr[i] < min:
                min = arr[i]

        print(f"The smallest number in array is {min}")
    else:
        print("The array is empty")


solve()
