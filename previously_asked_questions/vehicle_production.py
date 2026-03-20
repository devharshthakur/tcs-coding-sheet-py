"""
An automobile company manufactures both a two wheeler (TW) and a four wheeler (FW).
A company manager wants to make the production of both types of vehicle
according to the given data below:
- 1st data: Total number of vehicles (two-wheeler + four-wheeler) = V
- 2nd data: Total number of wheels = W

The task is to find how many two-wheelers as well as four-wheelers
need to be manufactured.
"""

# -------- logic ---------
# let x = two-wheelers, y = four-wheelers
# x + y = v
# 2x + 4y = w

# By solving the equations:
# y = (w - 2*v) / 2
# x = v - y
# --------- x ------------


def solve():
    v, w = 200, 540  # sample input

    # Simple check for edge cases
    if (w & 1) or w < 2 * v or w > 4 * v:
        return "INVALID INPUT"

    fw = (w - 2 * v) // 2
    tw = v - fw

    print(f"{tw} {fw}")


solve()
