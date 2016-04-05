""" ##PROBLEM
Hailstone Numbers.

Start with a small number, n, 1 <= n < 30.
There are two transformation rules that we will use:
  If n is odd, multiple by 3 and add 1 to create a new value for n.
  If n is even, divide by 2 to create a new value for n.

Perform a loop with these two transformation rules until you get to n = 1.
You’ll note that when n = 1, you get a repeating sequence of 1, 4, 2, 1, 4, 2, ...
The two interesting facts are the “path length”, the number of steps until you get to 1,
and the maximum value found during the process.
Tabulate the path lengths and maximum values for numbers 1..30.

Check: for 27, the path length is 111, and the maximum value is 9232.
"""

from random import randrange

number = randrange(1, 30)
print "random number chosen", number

max_number = number
steps = 0
while True:
    if number % 2 == 1:
        number = number * 3 + 1
        steps += 1
        if number == 1:
            break
        if number > max_number:
            max_number = number
    else:
        number = number / 2
        steps += 1
        if number == 1:
            break
        if number > max_number:
            max_number = number

print "maximum number", max_number
print "number of steps", steps
