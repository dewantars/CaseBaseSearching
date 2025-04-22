def abs(x):
    # Mengembalikan Nilai absolut dari x
    return x if x >= 0 else -x

def factorial(n):
    # Mengembalikan nilai faktorial dari n
    if n < 0:
        raise ValueError("Faktorial tidak didefinisikan untuk bilangan negatif")
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

def power(base, exp):
    # Mengembalikan nilai base pangkat exp
    result = 1
    for _ in range(abs(exp)):
        result *= base
    return result if exp >= 0 else 1 / result

def sin(x):
    # Menghitung nilai sin dari x (x dalam radian) menggunakan deret Taylor
    result = 0
    for i in range(20):  # Iterasi untuk konvergensi yang cukup baik
        term = power(-1, i) * power(x, 2 * i + 1) / factorial(2 * i + 1)
        result += term
    return result

def cos(x):
    # """Menghitung nilai cos dari x (x dalam radian) menggunakan deret Taylor"""
    result = 0
    for i in range(20):
        term = power(-1, i) * power(x, 2 * i) / factorial(2 * i)
        result += term
    return result

def tan(x):
    # """Menghitung nilai tan dari x (x dalam radian) sebagai sin/cos"""
    cosine = cos(x)
    if abs(cosine) < 1e-10:  # Menghindari pembagian dengan nol
        raise ValueError("tan tidak terdefinisi untuk nilai cos(x) mendekati nol")
    return sin(x) / cosine

def exp(x):
    # """Menghitung nilai e^x menggunakan deret Taylor"""
    result = 0
    for i in range(20):
        term = power(x, i) / factorial(i)
        result += term
    return result

def sqrt(x):
    # """Menghitung akar kuadrat menggunakan metode bisection"""
    if x < 0:
        raise ValueError("Akar kuadrat tidak terdefinisi untuk bilangan negatif")
    low, high = 0, x
    if x < 1:
        high = 1
    guess = (low + high) / 2
    while abs(guess * guess - x) > 1e-10:
        if guess * guess < x:
            low = guess
        else:
            high = guess
        guess = (low + high) / 2
    return guess

