"""Check if a array is a subset of another array"""


# Binary search algo
def binary_search(elem: int, arr: list[int]) -> bool:
    start = 0
    end = len(arr) - 1

    while start <= end:
        mid = (start + end) // 2

        if arr[mid] == elem:
            return True
        elif arr[mid] < elem:
            start = mid + 1
        else:
            end = mid - 1

    return False


# To check if arr1 is a subset of arr2
def is_subset(arr1: list, arr2: list[int]) -> bool:
    if len(arr1) > len(arr2):
        return False

    arr2.sort()

    for elem in arr1:
        if not binary_search(elem, arr2):
            return False

    return True


def solve():
    arr1 = [1, 3, 4, 5, 2]

    arr2 = [2, 4, 3, 1, 7, 5, 15]

    ans = is_subset(arr1, arr2)

    print(f"arr1 is {arr1}")
    print(f"arr2 is {arr2}")

    if ans:
        print("arr1[] is a subset of arr2[]")
    else:
        print("arr1[] is not a subset of arr2[]")


solve()
