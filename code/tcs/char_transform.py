"""
Problem: Character and Digit Transformation
Given a string and a value, transform each character as follows:
1. Alphabetic characters: shift by 'value' positions (with wraparound)
2. Digits: add 'value' and wrap around 0-9
3. Special characters: '@' becomes '#', any other becomes '@'

Example: input="abc@123", value=1
- 'a' -> 'b' (shift by 1)
- '@' -> '#'
- '1' -> '2' (add 1)
Output: "bcd#234"
"""


def add_value_to_chars(input_str, value):
    result = ""
    for char in input_str:
        # Check if character is alphabetic
        if char.isalpha():
            # Handle lowercase letters
            if char.islower():
                # Shift lowercase letter by value, wrapping around using modulo
                result += chr(((ord(char) - ord("a") + value) % 26) + ord("a"))
            # Handle uppercase letters
            else:
                # Shift uppercase letter by value, wrapping around using modulo
                result += chr(((ord(char) - ord("A") + value) % 26) + ord("A"))
        # Check if character is a digit
        elif char.isdigit():
            # Add value to digit and wrap around 0-9 using modulo
            result += str((int(char) + value) % 10)
        # Handle special characters
        else:
            # '@' becomes '#', any other special char becomes '@'
            if char == "@":
                result += "#"
            else:
                result += "@"
    return result


# Read input string and transformation value
input_str = input()
value = int(input())

# Transform the string
output_str = add_value_to_chars(input_str, value)
print("Output:", output_str)

# Time Complexity: O(n) - where n is length of input string
# Space Complexity: O(n) - for storing result string
