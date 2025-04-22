def factorial(n):
    if n < 0:
        raise ValueError("Faktorial tidak didefinisikan untuk bilangan negatif")
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

def power(base, exp):
    if exp == 0:
        return 1
    if exp < 0:
        return 1 / power(base, -exp)
    result = 1
    while exp > 0:
        if exp % 2 == 1:
            result *= base
        base *= base
        exp //= 2
    return result

def sin(x, epsilon=1e-12):
    x = x % (2 * 3.141592653589793)  # normalisasi sudut ke [0, 2π]
    result, term, i = 0, x, 1
    while abs(term) > epsilon:
        result += term
        term *= -x * x / ((2 * i) * (2 * i + 1))
        i += 1
    return result

def cos(x, epsilon=1e-12):
    x = x % (2 * 3.141592653589793)
    result, term, i = 1, 1, 1
    while abs(term) > epsilon:
        term *= -x * x / ((2 * i - 1) * (2 * i))
        result += term
        i += 1
    return result

def tan(x):
    c = cos(x)
    if abs(c) < 1e-12:
        raise ValueError("tan tidak terdefinisi untuk nilai cos(x) mendekati nol")
    return sin(x) / c

def exp(x, epsilon=1e-12):
    result, term, i = 1, 1, 1
    while abs(term) > epsilon:
        term *= x / i
        result += term
        i += 1
    return result

def sqrt(x, epsilon=1e-12):
    if x < 0:
        raise ValueError("Akar kuadrat tidak terdefinisi untuk bilangan negatif")
    if x == 0:
        return 0
    guess = x
    while True:
        next_guess = 0.5 * (guess + x / guess)
        if abs(guess - next_guess) < epsilon:
            return next_guess
        guess = next_guess

def abs(x):
    return x if x >= 0 else -x
