from operator import mul, sub
fact = (lambda f: lambda n: f(n, f))(lambda n, f: 1 if n == 0 else mul(n, f(sub(n, 1), f)))