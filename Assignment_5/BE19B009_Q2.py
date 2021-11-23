import matplotlib.pyplot as plt
from numpy import random
# no other libraries are allowed

def func(x):
    return 1/x

def Estimated_area_under_curve(func, lower_limit, higher_limit):
    """
    Estimate the area under the curve for a given function using the method discussed in the class using random numbers.
    Assume the input function to be monotonic.
    """
    maxruns = 100000                # Total number of throws
    maxvalue = 0                    # Initialising of the max value of function
    area = 0                        # Initialising area value
    runs = 0                        # Initialising run value

    # Since it is monotonic function, we have to check if its increasign or decreasing
    if (func(lower_limit) >= func(higher_limit)):
        maxvalue = func(lower_limit)            # Max value is f(lower_limit) for decreasing function
    else:
        maxvalue = func(higher_limit)           # Max value is f(higher_limit) for increasign function

    while runs < maxruns:
        y = random.uniform(0, maxvalue)                     # Pick a random-y from the area
        x = random.uniform(lower_limit, higher_limit)       # Pick a random-x from the area
        # print(x, y)
        if y <= func(x):                        # Check if the (x, y) is inside the area
            area += 1                       # Hence, increase the area
        runs = runs + 1                     # Also, increase the runs

    area = (higher_limit - lower_limit)*maxvalue*(area/maxruns)     # area = ratio*total_area
    return area

Estimated_area = Estimated_area_under_curve(func, 1/2, 2)

estimated_e = 0
# Find the area under the curve analytically. Equating the analytical expression and with the estimated value, find the value of the irrational number e. Hint, use log to the base 2.

# Do a base change to 2 from e to find the value of e
estimated_e = 2**(2/Estimated_area)

print("e = ", str(estimated_e))
