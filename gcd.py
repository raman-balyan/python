""" PROBLEM 
Greatest Common Diviser (GCD)

Find the GCD of the two inputs from the user.
"""


def greatest_common_divisor(num1, num2):
    """Return the GCD of the input numbers."""
    if num1 == num2:
        stop = num1
    elif num1 > num2:
        stop = num2
    else:
        stop = num1

    gcd = None
    for i in range(1, stop):
        if num1 % i == 0 and num2 % i == 0:
            if i > gcd:
                gcd = i

    return gcd

print greatest_common_divisor(21, 28)
