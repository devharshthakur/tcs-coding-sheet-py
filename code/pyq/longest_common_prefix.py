"""
Longest Common Prefix

You are given a list of strings. Your task is to find the longest common
prefix among all the strings in the list. If there is no common prefix,
return -1.

Input Format:
- First line: T (number of test cases)
- For each test case:
  - First line: N (number of strings)
  - Second line: space-separated strings

Output Format:
- For each test case, output the longest common prefix
- If no common prefix exists, output -1

Constraints:
- 1 ≤ T ≤ 100
- 1 ≤ N ≤ 100
- 1 ≤ |str| ≤ 100
- All strings consist of lowercase alphabetical characters

Example:
Input:
2
3
flower flow flight
2
dog racecar

Output:
fl
-1
"""


def solve():
    T = int(input("Enter no of test cases: "))

    for t in range(T):
        N = int(input(f"Enter no of strings in test case {t}: "))
        strings = input().split()
        prefix = ""

        for i in range(len(strings[0])):
            char = strings[0][i]

            valid = True
            for j in range(1, N):
                if i > len(strings[j]) or strings[j][i] != char:
                    valid = False
                    break

            if valid:
                prefix += char
            else:
                break

        if prefix == "":
            print(-1)
        else:
            print(prefix)


solve()
