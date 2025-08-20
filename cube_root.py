# the essential function: the SEARCH function

def search(check, update, guess=1):
    while not check(guess):
        guess = update(guess)
    return guess

def cbrt(a):
    def cbrt_check(x, tolerance=1e-7):
        return abs(x**3 - a) < tolerance
    def cbrt_update(x):
        # Newton's method
        return (2*x**3 + a) / (3*x**2) 
    return search(cbrt_check, cbrt_update)



"""draft:
y - (x1**3 - a) = 3*x1**2*(x - x1)
x1**3 - a + x* 3*x1**2 -3*x1**3 = 0
x = (2*x1**3 + a) / 3*x1**2
"""