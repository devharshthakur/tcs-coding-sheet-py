"""
Problem: Generate All Contiguous Substrings
Given a string of length n, generate all possible contiguous substrings
and print them in a specific format.

Format: Each substring is printed with characters space-separated,
different starting positions are separated by commas.

Example: Input "3 ABC"
- Starting at 0: "A" , "A B" , "A B C"
- Starting at 1: "B" , "B C"
- Starting at 2: "C"
Output: A,A B,A B C,B,B C,C
"""


def main():
    # Read input: first number is n, rest is the string
    in_str = input()
    arr = in_str.split(" ")
    n = int(arr[0])  # Length of string
    sb = "".join(arr[1:])  # Join remaining parts as the string

    # Outer loop: starting position (i)
    for i in range(n):
        # Middle loop: ending position (j)
        for j in range(i, n):
            # Inner loop: print characters from i to j
            for q in range(i, j + 1):
                # Print character with space if not the last one
                if q != j:
                    print(sb[q], end=" ")
                # Print last character without trailing space
                else:
                    print(sb[q], end="")
            # Add comma after substring if not the last starting position
            if i != n - 1:
                print(",", end="")
    # Print newline at the end
    print()


if __name__ == "__main__":
    main()

# Time Complexity: O(n^3) - three nested loops
# Space Complexity: O(1) - only using input variables
