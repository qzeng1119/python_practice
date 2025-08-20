def average(x, y):
    return (x + y) / 2

def improve(update, close, guess=1):
    while not close(guess):
        guess = update(guess)
    return guess
"""
this function is kind of like the "search function":
(1) first get one random guess, check if the guess is what we want: // by using the "check function"
    if it is, then return the guess, we are done;
    otherwise, update the guess to a better one  // by using the "update function"
(2)repeat until we find the guess we want

the template is as below:
def search(<functioin> check, <function> update, <variable> guess=initial guess):
    while not check(guess):
        guess = update(guess)
    return guess
"""   

def sqrt(a):
    def sqrt_update(x):
        return average(x, a/x)
    def sqrt_close(x, tolerance=1e-7):
        return abs(x*x - a) < tolerance
    return improve(sqrt_update, sqrt_close)
