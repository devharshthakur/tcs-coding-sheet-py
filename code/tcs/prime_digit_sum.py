"""
Problem: Prime Numbers with Prime Digit Sum
Given a range [n, m], find all numbers that satisfy two conditions:
1. The number itself is prime
2. The sum of its digits is also prime

Example: If range is [10, 20]
- 13 is prime and digit sum (1+3=4) is not prime - skip
- 17 is prime and digit sum (1+7=8) is not prime - skip
- 19 is prime and digit sum (1+9=10) is not prime - skip
"""


def isPrime(number):
    # Numbers <= 1 are not prime
    if number <= 1:
        return False
    # 2 and 3 are prime
    if number <= 3:
        return True
    # Numbers divisible by 2 or 3 are not prime
    if number % 2 == 0 or number % 3 == 0:
        return False
    # Check divisibility by numbers of form 6k±1 up to sqrt(number)
    i = 5
    while i * i <= number:
        if number % i == 0 or number % (i + 2) == 0:
            return False
        i += 6
    return True


def calculateSum(n):
    # Calculate sum of digits
    sum = 0
    while n > 0:
        num = n % 10
        sum += num
        n //= 10
    # Check if digit sum is prime
    if isPrime(sum):
        return True
    else:
        return False


# Read range [n, m] from input
n, m = map(int, input().split())
# Find and print numbers that are prime AND have prime digit sum
for i in range(n, m + 1):
    if isPrime(i) and calculateSum(i):
        print(i)
