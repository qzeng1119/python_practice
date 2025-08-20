def decorator(f):
    """Take a one-argument function F as argument and return
    another function which is the decorated F. The decorated
    function has the same formal parameter as F. 
    """
    def decorated(x):
        print("Calling", f, "on the argument", x)
        return f(x)
    return decorated

# to decorate a function using 'decorator', we have two ways
way = 1 # change the 'way' between 0 and 1 to try different ways of decoration

if way:
    # the first way: a more common and better way
    @decorator
    def square(x):
        return x * x
else:
    # the second way:
    def square(x):
        return x * x
    square = decorator(square)

    