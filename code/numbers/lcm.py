def gcd(a: int, b: int):
    """Find GCD"""
    while b != 0:
        a, b = b, a % b
    gcd = a
    return gcd


def solve():
    """Find LCM using Eculidien algo"""

    a = int(input("Enter value of a: "))
    b = int(input("Enter value of b: "))

    lcm = (a * b) // gcd(a, b)
    print(f"LCM of {a} and {b} is {lcm}")


solve()
